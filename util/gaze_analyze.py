"""
    Gaze Analyze
    ~~~~~~~~~~~~
"""

def calculate_impaction(avg_fix, avg_sac, avg_reg):
    """
    Calculate the impaction by using gaze information
    There are three parameters, (weight of fixation, saccade, regression)
    Optimize it heuristically and use it to decide difficulty of reading

    :param avg_fix: Average fixation time
    :param avg_sac: Average saccade time
    :param avg_reg: Average regression time
    :return: Impaction of gaze calculated
    """

    avg_fix_param = 0.01
    avg_sac_param = 100
    avg_reg_param = 100

    try:
        print (avg_fix, avg_sac, avg_reg)
        print (avg_fix_param * avg_fix) + (avg_sac_param * avg_sac) + (avg_reg_param * avg_reg)
        return (avg_fix_param * avg_fix) + (avg_sac_param * avg_sac) + (avg_reg_param * avg_reg)
    except:
        return 0

def analyze(word, duration, start, end, word_idx, sentences):
    """
    Get information of gaze collected by using eye-tracker.
    Processing information to call calculate-impaction function.
    If impaction is larger than threshold, clear word, duration, start, end list
    It means user feel difficult to read this picture.

    :param word: Recently read word
    :param duration: Fixation time of each word in word list
    :param start: Starting word index in gaze information (e.g. Saccade)
    :param end: Ending word index in gaze information (e.g. Saccade)
    :param word_idx: Index of word
    :param sentences: Index of sentence
    :return:
    """
    threshold = 29
    parsed_fixation = {}
    idx = 0
    for w_idx in word_idx:
        for k_idx in sorted(sentences.keys()):
            if int(w_idx) < k_idx:
                try:
                    if int(duration[idx]) > 4000:
                        continue
                    parsed_fixation[k_idx].append([int(duration[idx]), int(start[idx]), int(end[idx]), int(w_idx)])
                except:
                    parsed_fixation[k_idx] = [[int(duration[idx]), int(start[idx]), int(end[idx]), int(w_idx)]]
                break
        idx += 1
    # print parsed_fixation

    for key, value in parsed_fixation.items():

        average_fixation = 0

        average_saccade = 0

        average_regression = 0

        num_saccade = 0
        num_regression = 0

        for v_i, v in enumerate(value[:-1]):
            average_fixation += v[0]
            # max_fixation = max(max_fixation, v[0])
            if v[3] < value[v_i + 1][3]:
                try:
                    average_saccade += (value[v_i + 1][3] - v[3])/float(value[v_i + 1][1] - v[2])
                    num_saccade += 1
                except:
                    pass
                # max_saccade = max(max_saccade, (value[v_i + 1][3] - v[3])/float(value[v_i + 1][1] - v[2]))
            if v[3] > value[v_i + 1][3]:
                try:
                    average_regression += (v[3] - value[v_i + 1][3])/float(value[v_i + 1][1] - v[2])
                    num_regression += 1
                except:
                    pass
                # max_regression = max(max_regression, (v[3] - value[v_i + 1][3])/float(value[v_i + 1][1] - v[2]))

        average_fixation += value[-1][0]
        # max_fixation = max(max_fixation, value[-1][0])

        average_fixation /= len(value)
        try:
            average_saccade /= num_saccade
        except:
            average_saccade = 0
        try:
            average_regression /= num_regression
        except:
            average_regression = 0

        print ("Fixation", average_fixation)
        print ("Saccade", average_saccade)
        print ("Regression", average_regression)

        # if (average_saccade < 0.01):
        #     return word, duration, start, end, word_idx
        if calculate_impaction(average_fixation, average_saccade, average_regression) > threshold and len(value) > 6:
            print ("-"*200)
            print ("RESET")
            print ("-"*200)
            word = []
            duration = []
            start = []
            end = []
            word_idx = []
            return word, duration, start, end, word_idx
    return word, duration, start, end, word_idx