import os
import json
from json import JSONEncoder
from dataclasses import dataclass
from datetime import datetime, timedelta


class Agent:
    
    def __init__(self, filepath, boxes=None):
        
        self.filepath = filepath
        self.boxes = boxes if boxes is not None else []
        
        
    def read_in_boxes_from_file(self):
        
        with open(os.path.join(os.getcwd(), self.filepath), 'r') as f:
            boxes_dicts = json.loads(f.read())['boxes']
            
        boxes = []
        for box_dict in boxes_dicts:
            contents = box_dict['contents']
            frequency = box_dict['freq']

            flashcards = self.build_flashcards_from_json(contents)
            box = self.build_box_from_json(flashcards, frequency)
            
            boxes.append(box)
                
        self.boxes = boxes
        
        
    def build_flashcards_from_json(self, data):
        
        flashcards = []
        for fc in data:
            q = fc['question']
            a = fc['answer']
            c_b = fc['current_box']
            a_n = datetime.fromisoformat(fc['answer_next']['iso'])
            flashcard = Flashcard(q, a, c_b, a_n)
            flashcards.append(flashcard)
            
        return flashcards
    
    
    def build_box_from_json(self, flashcards, freq):
        frequency = timedelta(days=freq['days'], seconds=freq['seconds'], microseconds=freq['microseconds'])
        return Box(flashcards, freq)

    
    def save_boxes_to_file(self):
        
        if os.path.exists(t := os.path.join(os.getcwd(), self.filepath)):
            x = input(f'Are you sure you would like to overwrite file {t}? -press- "Y/y" for Yes or Any key to Quit: ')
            if x.upper() == 'Y':
                print('Overwriting...')
            else:
                print('Aborting...')
                
        with open(os.path.join(os.getcwd(), self.filepath), 'w') as f:
            agent_data = json.dumps(self, indent=4, cls=AgentEncoder) # remove indent for compact storage? YES DUH, WAY BETTER STORAGE SIZE LIKE HOLY SHIT
            f.write(agent_data)
            

@dataclass
class Box:
    
    contents: list=None
    freq: timedelta=timedelta(days=1)
        
    def __post_init__(self):
        if isinstance(self.freq, int) or isinstance(self.freq, float):
            self.freq = timedelta(seconds=self.freq)

        if not isinstance(self.freq, timedelta):
            raise TypeError('frequency value must be a timedelta object, int, or float. {self.freq=} is {type(self.freq)=}')

        
@dataclass
class Flashcard:
    
    question: str = '1+1'
    answer: str = '2'
    current_box: int = 1
    answer_next: datetime = datetime.now()
        
        
class AgentEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(o, timedelta):
            return dict(days=o.days, seconds=o.seconds, microseconds=o.microseconds)
        if isinstance(o, datetime):
            return dict(iso=o.isoformat())
        return o.__dict__
