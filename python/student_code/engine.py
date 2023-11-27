'''
Provides template code to automatically make decisions for the autonomous
car.
'''
from scenario import Scenario

def decide(scenario):
    """ Decides whether your car will save the passengers or pedestrians

    Args:
        scenario: a Scenario object defined in scenario.py. This object contains
            all of the information about the scenario. You can see some
            examples below in the sample code.

    Returns:
        A string indicating whether you are saving "passengers" or
        "pedestrians". Note that your method MUST make a decision for
        ANY potential scenario.
    """
    pas = 0
    ped = 0
    # NOTE: YOU NEED TO REPLACE ALL OF THE CODE BELOW!!!
    # This simply demonstrates how to access information from the scenario.
    # print("Are the pedestrians crossing legally?", scenario.legalCrossing)
    # print("Is the car in the same lane as the pedestrians?", scenario.pedsInLane)
    # print("Are you in car?", scenario.youInCar)
    #
    # print("Print whether each pedestrian is a human, animal, or you")
    # for person in scenario.pedestrians:
    #     print(person.charType)


    # Your program must choose to save either pedestrians or passengers.
    # This is an overly simple rule that only saves the passengers if there are
    # more passengers than pedestrians.
    for Person in scenario.pedestrians:
        if(Person.charType != "animal"):
            ped += 1
        if(Person.age == "child" or Person.age == "baby"):
            ped += 3
        if(Person.age == "adult"):
            ped += 2
        if(Person.age == "elderly"):
            ped += 1
        if(Person.profession == "doctor"):
            ped += 1
        if(Person.profession == "criminal"):
            ped -= 1
        if(Person.pregnant):
            ped += 1
    for Person in scenario.passengers:
        if(Person.charType != "animal"):
            pas += 1
        if(Person.age == "child" or Person.age == "baby"):
            pas += 3
        if(Person.age == "adult"):
            pas += 2
        if(Person.age == "elderly"):
            pas += 1
        if(Person.profession == "doctor"):
            pas += 1
        if(Person.profession == "criminal"):
            pas -= 1
        if(Person.pregnant):
            pas += 1
    if ped > pas:
        return "pedestrians"
    else:
        return "passengers"
