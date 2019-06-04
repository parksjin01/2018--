# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from server import parsing

# test_set = ["Eating strawberries without washing them might make you sick.", "They were painting their house when it started to rain.", "I’ve been thinking about going shopping on Saturday.", "Jennifer is always baking something in the kitchen.", "Thanks for taking off your shoes before coming in the house.", "Jill is playing the violin with the bow Jerry bought her when they went to Italy.", "The kids were excited about eating birthday cake.", "He was taking a picture when lightning struck.", "Running for president is a serious ambition.", "Eating small meals throughout the day can help you avoid hunger pains.", "A serious danger to motorists is driving under the influence.", "Keeping a light on in the house helps discourage robbers."]
# test_set = ["If I had been more careful, I could have gotten a full mark in English",
# "If Steve had finished the project successfully, he could have been promoted.",
# "If Susan had not been sick then, she could have attended the meeting.",
# "If it had not rained yesterday, we could have gone camping.",
# "What would have happened if I hadn't checked the room?",
# "If I had slept well last night, I would not be very tired now.",
# "If he hadn't gone to the Vietnam War, he should be 57 by now."]
# test_set = ["The reporter who is held as a hostage by the terrorist is my cousin.",
# "We're talking about a child who died, not a living patient.",
# "I don't want to criticise those that provide private care",
# "The buildings which were built illegally will be torn down.",
# "The car which she bought yesterday is a used car.",
# "That is the spacecraft that the first Korean astronaut is aboard.",
# "She is the author whom the prosecutor accused of a crime.",
# "I ate dinner with my ex-girlfriend that I hadn't seen for years."]
test_set = ["A person whose job is to handle human relations can describe their job performances clearly."]

res = []

for sentence in test_set:
    parsing(sentence, 0, res)