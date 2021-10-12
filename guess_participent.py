import random

participants = ['Jack','Jill','Larry','Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
        print(participant, my_participant_dict[participant])
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False
    
print(Guess(participants))
