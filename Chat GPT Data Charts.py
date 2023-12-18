'''
Dilshawn Dhaliwal
ChatGPT Assignment Code
'''
# Import all of the modules
import matplotlib.pyplot as plt
import pandas as pd

# Change the default font size for matplotlib charts
plt.rcParams['font.size'] = 9.0


# ========= FUNCTIONS =========
'''
Get the list of all answers to a question
  file: the excel file to read from
  question: the question from the excel sheet, as a string
'''
def getList(file, question):
    return list(file[question])


'''
Get the answers to the question and return them as 2 lists:
One with the possible answers (string), another with the # of times each option was chosen.
Single choice questions only.
  question: The answer list from the question in the excel sheet.
'''
def getAnswers(question):
    # Use a dictionary to track how many times each answer was chosen
    answerDict = {}
    # For each answer in the question list:
    for i in range(0, len(question)):
        answer = question[i]
        # if the answer is not currently in the dictionary, add it and set it to 1
        if answer not in answerDict:
            answerDict[answer] = 1
        # Otherwise, increment its count by 1
        else:
            answerDict[answer] = answerDict[answer] + 1

    # returns a list containing each answer as text, and how many times they were chosen
    return [list(answerDict.keys()), list(answerDict.values())]


'''
Get each individual answer from the multiple choice question. Return 2 lists in a list:
List 1 has the possible answers.
List 2 has the count for each answer.
  question: the question from the excel sheet.
  choices: possible choices to the question
'''
def getMultiAnswers(question, choices):
    answerDict = {} # Dictionary is used to track answers and their responses.
    
    # For each possible answer in choices, make a key for it in the dictionary.
    for i in choices:
        answerDict[i] = 0

    # For each participants response
    for i in range(0, len(question)):
        # Their answer is saved here, as a list seperated by commas and space (how it's done in excel)
        answers = question[i].split(", ")
        # For each selected asnwer, increment its count by 1
        for j in answers:
            answerDict[j] = answerDict[j] + 1
            
    return [list(answerDict.keys()), list(answerDict.values())]

    
'''
Make a bar graph for a multiple choice question
 question: the question list
 answers: possible answers to the question
 axis: the axis to plot the graph on
 x, y: x and y locaations to place the graph on the subplots grid.
 xtitle, ytitle: titles for the x and y axis of the bar graph
 font: the font size of the bar labels
'''
def makeBarGraph(question, answers, axis, x, y, title, xtitle, ytitle, font = 9):
    # use the getMultiAnswers method to get the answers and counts
    ans = getMultiAnswers(question, answers)
    # Set the title of the main graph
    axis1[y][x].set_title(title)
    # Make the bar graph
    axis1[y][x].barh(list(range(0, len(ans[0]))), ans[1], color = 'orange')

    # Set x and y axis titles
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    
    # Set the ticks for the y-axis 
    plt.yticks(ticks = list(range(0, len(ans[0]))), labels = ans[0])

    # Put labels on the bars showing their values
    for i in axis[y][x].patches:
        plt.text(i.get_width()-5, i.get_y()+0.3, str(round((i.get_width()), 2)),
                 fontsize = font)
        
        
'''
Make a pie chart for a subplot. Parameters are used in the creation of the chart.
  question: The question's answers from the excel sheet.
  axis: the variables from plt.subplots().
  x, y: the x and y locations of the chart in the grid
  title: The title of the subplot graph.
  font: Set font size for the labels, default is 9
  angle: Set starting angle for the pie chart, default is 0

Angle and Font are used for formatting purposes.
'''
def makePieChart(question, axis, x, y, title, font = 9, angle = 0):
    # Use getAnswers to get the list of responses and their counts
    answers = getAnswers(question)
    
    # Create subplot graph and set title of the subplot graph
    axis[y][x].pie(answers[1], labels = answers[0], autopct='%1.1f%%', textprops={'fontsize': font}, startangle = angle)
    axis[y][x].set_title(title)
    

'''
Get data from question1 from people who answered question 2 with the 'condition' variable
 Example: Get opinions on plagiarism (q1)
 from people who answered '18 - 24' (condition) to the age question (q2)
 Note: This code is compatable with single and multiple choice questions.

 question1: The question to receive data from.
 question2: The question that houses the conditon.
 condition: The condition to receive data from question1.
'''
def getSubData(question1, question2, condition):
    result = []
    # For each index in questions (question lists are all same length)
    for i in range(0, len(question1)):
        # if the condition is in their answer to question2
        if condition in question2[i]:
            # Put question1's answer in the result list
            result.append(question1[i])

    # Return results list, which is question1 but only with answers that people chose alongside the condition.
    return result
            
        

# =========== MAIN PROGRAM ===========

if __name__ == "__main__":
    # Import the excel file. File must be in the same directory as this program.
    f = pd.read_excel("Group 94 Data.xlsx")
    
    # Creating lists for each independent variable (1-5)
    ages = getList(f, "What is your age?")
    genders = getList(f, "What is your gender?")
    positions = getList(f, "What is your academic position?")
    faculties = getList(f, "What academic faculty are you in?")
    occupations = getList(f, "Which of the following are you a part of? Select all that apply.")
    
    # Making lists for each dependent variable (6-10)
    known = getList(f, "How much do you know about Chat GPT?")
    used = getList(f, "Have you ever used Chat GPT?")
    plagiarism = getList(f, "How often do you believe that using Chat GPT for academic assignments counts as plagiarism?")
    learning = getList(f, "Do you think that using Chat GPT would ultimately harm or help a student's learning?")
    benefits = getList(f, "Which demographic would receive the most legitimate benefit (benefit which does not violate any rules or laws) from using Chat GPT?")


    
    
    # ========== GRAPH 1: INDEPENDENT VARIABLE GRAPHS ==========
    # Multiple graphs in one window. This makes a 3x2 grid. 
    fig1, axis1 = plt.subplots(2,3, figsize = (11,6))
    # Hide the unused grid section. Set the title.
    axis1[1][1].set_visible(False)
    fig1.suptitle("Independent Variable Graphs (102 Participants)")
    
    # Make the pie graphs
    makePieChart(ages,      axis1,  0, 0, "Age of Participants")
    makePieChart(genders,   axis1,  1, 0, "Gender of Participants", 9, -10)
    makePieChart(positions, axis1,  2, 0, "Academic Position of Participants",9, 15)
    makePieChart(faculties, axis1,  0, 1, "Faculty of Participants")

    # Need a bar graph for extracurriculars
    makeBarGraph(occupations, ["Full time job", "Part time job", "Extracurricular club", "Volunteering", "None"],
                 axis1, 2, 1, "Extracurriculars of Participants (114 chosen answers)", "No. of Participants", "Extracurriculars")


    
    
    # =========== GRAPH 2: DEPENDENT VARIABLE GRAPHS ===========
    # Making a 3x2 grid.
    fig2, axis2 = plt.subplots(2,3, figsize = (11,6))
    # Hide unused grid section and set title
    axis2[1][1].set_visible(False)
    fig2.suptitle("Dependent Variable Graphs (102 participants)")

    # Make the pie graphs
    # Font and angle are altered to ensure formatting does not interfere with other graphs
    makePieChart(known,         axis2,  0, 0, "Participant Knowledge of ChatGPT", 7.75, 125)
    makePieChart(learning,      axis2,  1, 0, "Benefits vs Harm on Students' Learning", 9, -45)
    makePieChart(used,          axis2,  2, 0, "Participant Usage of ChatGPT", 9, 90)
    makePieChart(plagiarism,    axis2,  0, 1, "Thoughts on ChatGPT as Plagiarism", 8, 180)
    makePieChart(benefits,      axis2,  2, 1, "Who would receive the most benefit from ChatGPT", 8, 90)



    
    # ========== GRAPH 3: COMPARING OPINIONS ON CHAT GPT PLAGIARISM AND BENEFITS BY POSITION ==========
    # Initializing Graph
    fig3, axis3 = plt.subplots(2,3, figsize = (11,6))
    axis3[0][1].set_visible(False)
    axis3[1][1].set_visible(False)
    fig3.suptitle("Opinions on ChatGPT and its Benefits by Academic Position")
    
    # Getting Student Learning data from respective faculty
    learningStudents = getSubData(learning, positions, "Student")
    learningProfs = getSubData(learning, positions, "Professor")
    learningTA = getSubData(learning, positions, "Teacher Assistant")
    learningOther = getSubData(learning, positions, "Other")
    # Extending Professors, since it is students vs other faculty memebers for comparison.
    learningProfs.extend(learningTA)
    learningProfs.extend(learningOther)
    
    # Make Student Learning charts
    makePieChart(learningStudents,   axis3, 0,0, "Students' thoughts on Student Learning with ChatGPT\n(95 Responses)", 10, 20)
    makePieChart(learningProfs,   axis3, 2,0, "Professor, T.A., and Other Faculty Positions' thoughts Student Learning with ChatGPT\n(7 Responses)", 10, 20)

    # Getting faculty's data for benefits
    benefitsStudents = getSubData(benefits, positions, "Student")
    benefitsProfs = getSubData(benefits, positions, "Professor")
    benefitsTA = getSubData(benefits, positions, "Teacher Assistant")
    benefitsOther = getSubData(benefits, positions, "Other")
    # Extending Professors list, since it is students vs other faculty memebers for comparison.
    benefitsProfs.extend(benefitsTA)
    benefitsProfs.extend(benefitsOther)
    
    # Make Benefit opinion graphs
    makePieChart(benefitsStudents,   axis3, 0,1, "Student thoughts on who ChatGPT Benefits the Most\n(95 Responses)", 9, 20)
    makePieChart(benefitsProfs,   axis3, 2,1, "Professor, T.A., and Other Position thoughts on who ChatGPT Benefits the Most\n(7 Responses)", 9, 20)



    
    # ========== GRAPH 4: COMPARING USAGE, KNOWLEDGE, AND PLAGIARISM OF CHATGPT BY ACADEMIC POSITION ==========
    # Initialize graph
    fig4,axis4 = plt.subplots(2,2, figsize = (11,6))
    fig04,axis04 = plt.subplots(2,2, figsize = (11,6))
    fig004,axis004 = plt.subplots(2,2, figsize = (11,6))

    # Split up among 3 subplots to ensure graphs are not tiny.
    axis4[1][0].set_visible(False)
    axis4[1][1].set_visible(False)
    axis04[1][0].set_visible(False)
    axis04[1][1].set_visible(False)
    axis004[1][0].set_visible(False)
    axis004[1][1].set_visible(False)
    
    fig4.suptitle("Knowledge on ChatGPT by Academic Position")
    fig04.suptitle("Usage of ChatGPT by Academic Position")
    fig004.suptitle("Opinions on ChatGPT and Plagiarism by Academic Position")

    # Get Knowledge data for each position
    knownStudents = getSubData(known, positions, "Student")
    knownProfs = getSubData(known, positions, "Professor")
    knownTA = getSubData(known, positions, "Teacher Assistant")
    knownOther = getSubData(known, positions, "Other")
    knownProfs.extend(knownTA)
    knownProfs.extend(knownOther)
    
    # Make knowledge graphs
    makePieChart(knownStudents, axis4, 0,0, "Student Knowledge on ChatGPT\n(95 Responses)", 9, 90)
    makePieChart(knownProfs, axis4, 1,0, "Professor, TA, and Other Position Knowledge on ChatGPT\n(7 Responses)", 9, 90)

    # Get Usage Data for each position
    useStudents = getSubData(used, positions, "Student")
    useProfs = getSubData(used, positions, "Professor")
    useTA = getSubData(used, positions, "Teacher Assistant")
    useOther = getSubData(used, positions, "Other")
    useProfs.extend(useTA)
    useProfs.extend(useOther)

    # Make Usage graphps
    makePieChart(useStudents, axis04, 0,0, "Student Usage of ChatGPT\n(95 Responses)",9, 90)
    makePieChart(useProfs, axis04, 1,0, "Professor, TA, and Other Position Usage of ChatGPT\n(7 Responses)",9, 90)

    # Get Plagiarism Data for each position
    PlagiarismSt = getSubData(plagiarism, positions, "Student")
    PlagiarismProf = getSubData(plagiarism, positions, "Professor")
    PlagiarismTA = getSubData(plagiarism, positions, "Teacher Assistant")
    PlagiarismOther = getSubData(plagiarism, positions, "Other")
    PlagiarismProf.extend(PlagiarismTA)
    PlagiarismProf.extend(PlagiarismOther)
    
    # Make Plagiarism Pie Charts
    makePieChart(PlagiarismSt, axis004, 0,0, "Student Thoughts on Plagiarism and ChatGPT\n(95 Responses)", 9, 180)
    makePieChart(PlagiarismProf, axis004, 1,0, "Professor, TA, and Other Position Thoughts on Plagiarism and ChatGPT\n(7 Responses)")



    
    # ========== GRAPH 5: KNOWLEDGE OF CHATGPT BY ACADEMIC FACULTY ===========
    fig5, axis5, = plt.subplots(2,3, figsize = (11,6))
    axis5[1][1].set_visible(False)
    fig5.suptitle("Knowledge of ChatGPT BY Academic Faculty")

    # Get Knowledge graphs by position
    knownArt = getSubData(known, faculties, "Arts")
    knownSci = getSubData(known, faculties, "Science")
    knownEng = getSubData(known, faculties, "Engineering")
    knownBus = getSubData(known, faculties, "Business")
    knownLaw = getSubData(known, faculties, "Law")
    knownOther = getSubData(known, faculties, "Other")
    # Law had 1 response, including it in other.
    knownOther.extend(knownLaw)
    # Make Graphs for Graph 5
    makePieChart(knownArt ,axis5, 0,0, "Art\n(16 Responses)", 7, 120)
    makePieChart(knownSci ,axis5, 1,0, "Science\n(67 Responses)",7, 15)
    makePieChart(knownEng ,axis5, 2,0, "Engineering\n(3 Responses)", 7, -40)
    makePieChart(knownBus ,axis5, 0,1, "Business\n(7 Responses)", 8, -60)
    makePieChart(knownOther ,axis5, 2,1, "Law & Other\n(9 Responses)", 8, -45)




    # ========== GRAPH 6: USAGE BY FACULTY ==========
    fig6, axis6, = plt.subplots(2,3, figsize = (11,6))
    axis6[1][1].set_visible(False)
    fig6.suptitle("Usage of ChatGPT BY Academic Faculty")
    
    usedArt = getSubData(used, faculties, "Arts")
    usedSci = getSubData(used, faculties, "Science")
    usedEng = getSubData(used, faculties, "Engineering")
    usedBus = getSubData(used, faculties, "Business")
    usedLaw = getSubData(used, faculties, "Law")
    usedOther = getSubData(used, faculties, "Other")
    # Merge Law and Other
    usedOther.extend(usedLaw)
    # Make Graphs for Graph 6
    makePieChart(usedArt ,axis6, 0,0, "Art\n(16 Responses)")
    makePieChart(usedSci ,axis6, 1,0, "Science\n(67 Responses)")
    makePieChart(usedEng ,axis6, 2,0, "Engineering\n(3 Responses)")
    makePieChart(usedBus ,axis6, 0,1, "Business\n(7 Responses)")
    makePieChart(usedOther ,axis6, 2,1, "Law & Other\n(9 Responses)")



    
    # ========== GRAPH 7: PLAGIARISM OPINIONS BY FACULTY ==========
    fig7, axis7, = plt.subplots(2,3, figsize = (11,6))
    axis7[1][1].set_visible(False)
    fig7.suptitle("Opinions on ChatGPT and Plagiarism by Academic Faculty")
    
    plagArt = getSubData(plagiarism, faculties, "Arts")
    plagSci = getSubData(plagiarism, faculties, "Science")
    plagEng = getSubData(plagiarism, faculties, "Engineering")
    plagBus = getSubData(plagiarism, faculties, "Business")
    plagLaw = getSubData(plagiarism, faculties, "Law")
    plagOther = getSubData(plagiarism, faculties, "Other")

    plagOther.extend(plagLaw)
    # Make Graphs for Graph 7
    makePieChart(plagBus, axis7, 0,0, "Business\n(7 Responses)",7.5)
    makePieChart(plagEng, axis7, 1,0, "Engineering\n(3 Responses)",7.5, -155)
    makePieChart(plagOther, axis7, 2,0, "Law & Other\n(9 Responses)", 7.5, -60)
    makePieChart(plagSci, axis7, 0,1, "Science\n(67 Responses)",7.5, -15)
    makePieChart(plagArt, axis7, 2,1, "Art\n(16 Responses)",7.5, -135)



    
    # ========== GRAPH 8: BENEFITS VS HARMS TO STUDENT LEARNING BY ACADEMIC FACULTY ==========
    fig8, axis8, = plt.subplots(2,3, figsize = (11,6))
    axis8[1][1].set_visible(False)
    fig8.suptitle("Thoughts on Student Learning with ChatGPT by Academic Faculty")
    
    learnArt = getSubData(learning, faculties, "Arts")
    learnSci = getSubData(learning, faculties, "Science")
    learnEng = getSubData(learning, faculties, "Engineering")
    learnBus = getSubData(learning, faculties, "Business")
    learnLaw = getSubData(learning, faculties, "Law")
    learnOther = getSubData(learning, faculties, "Other")

    learnOther.extend(learnLaw)
    # Make Graphs
    makePieChart(learnArt, axis8, 0,0, "Art\n(16 Responses)")
    makePieChart(learnSci, axis8, 1,0, "Science\n(67 Responses)")
    makePieChart(learnEng, axis8, 2,0, "Engineering\n(3 Responses)")
    makePieChart(learnBus, axis8, 0,1, "Business\n(7 Responses)")
    makePieChart(learnOther, axis8, 2,1, "Law & Other\n(9 Responses)")



    
    # ========== GRAPH 9: WHO BENEFITS FROM CHATGPT BY ACADEMIC FACULTY ==========
    fig9, axis9, = plt.subplots(2,3, figsize = (11,6))
    axis9[1][1].set_visible(False)
    fig9.suptitle("Who ChatGPT Benefits by Academic Faculty")
    
    benefitArt = getSubData(benefits, faculties, "Arts")
    benefitSci = getSubData(benefits, faculties, "Science")
    benefitEng = getSubData(benefits, faculties, "Engineering")
    benefitBus = getSubData(benefits, faculties, "Business")
    benefitLaw = getSubData(benefits, faculties, "Law")
    benefitOther = getSubData(benefits, faculties, "Other")

    benefitOther.extend(benefitLaw)
    # Make Graphs for graph 9
    makePieChart(benefitArt, axis9, 0,0, "Art\n(16 Responses)", 9, 180)
    makePieChart(benefitSci, axis9, 1,0, "Science\n(67 Responses)")
    makePieChart(benefitEng, axis9, 2,0, "Engineering\n(3 Responses)")
    makePieChart(benefitBus, axis9, 0,1, "Business\n(7 Responses)")
    makePieChart(benefitOther, axis9, 2,1, "Law & Other\n(9 Responses)", 9, -90)
    
    # Show all graphs
    plt.show()

