# Copyright 2021 Spirent Communications.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Tool to suggest which ML approach is more applicable for
a particular data and usecase.
"""


from __future__ import print_function
import signal
import sys
from pypsi import wizard as wiz
from pypsi.shell import Shell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class AlgoSelectorWizard(object):
    """
    Class to create wizards
    """
    def __init__(self):
        """
        Perform Initialization.
        """
        self.shell = Shell()
        self.main_values = {}
        self.gen_values = {}
        self.supervized_values = {}
        self.unsupervized_values = {}
        self.reinforced_values = {}
        self.wiz_main = None
        self.wiz_main_l1 = None
        self.wiz_main_l2_a = None
        self.wiz_main_l2_b = None
        self.wiz_main_l3 = None
        self.wiz_main_l4 = None
        self.wiz_supervized = None
        self.wiz_unsupervized = None
        self.wiz_reinforced = None


    ############# All the Wizards ##################################

    ### GENERIC Wizards - Need for ML ##############################
    def main_wizard_l1(self):
        """
        The Main Wizard L1
        """
        self.wiz_main_l1 = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Do you Need ML - Data Availability"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_availability",
                    # Display name
                    name=bcolors.HEADER+"Do you have access to data about different situations, or that describes a lot of examples of situations"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U - Yes/No/Unknown",
                    validators=(wiz.required_validator),
                    default='Y',
                ),
            )
        )

    def main_wizard_l2_a(self):
        """
        The Main Wizard L2-A
        """
        self.wiz_main_l2_a = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Do you Need ML - Data Creation"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_creativity",
                    # Display name
                    name=bcolors.HEADER+"Will a system be able to gather a lot of data by trying sequences of actions in many different situations and seeing the results"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U - Yes/No/Unknown",
                    validators=(wiz.required_validator),
                    default='Y',
                ),
            )
        )
    
    def main_wizard_l2_b(self):
        """
        The Main Wizard L2-B
        """
        self.wiz_main_l2_b = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Do you Need ML - Data Programmability"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_programmability",
                    # Display name
                    name=bcolors.HEADER+"Can a program or set of rules decide what actions to take based on the data you have about the situations"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U - Yes/No/Unknown",
                    validators=(wiz.required_validator),
                    default='Y',
                ),
            )
        )


    def main_wizard_l3(self):
        """
        The Main Wizard L3
        """
        self.wiz_main_l3 = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Do you Need ML - Data Knowledge"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_knowledge",
                    # Display name
                    name=bcolors.HEADER+"Could a knowledgeable human decide what actions to take based on the data you have about the situations"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U - Yes/No/Unknown",
                    validators=(wiz.required_validator),
                    default='Y',
                ),
            )
        )

    def main_wizard_l4(self):
        """
        The Main Wizard - L4
        """
        self.wiz_main_l4 = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Do you Need ML - Data Pattern"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_pattern",
                    # Display name
                    name=bcolors.HEADER+"Could there be patterns in these situations that the humans haven't recognized before"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U - Yes/No/Unknown",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
            )
        )
    ### GENERIC Wizards - GOAL, METRICS, DATA ##############################
    def gen_wizard(self):
        """
        Generic Wizard - Goal, metrics, data
        """
        self.wiz_generic = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Understanding Goal, Metrics, Data and Output Type"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_goal",
                    # Display name
                    name=bcolors.HEADER+" What is your goal with the data? Predict, Describe or Explore"+bcolors.ENDC,
                    # Help message
                    help="Enter one of Predict/Describe/Explore",
                    validators=(wiz.required_validator),
                    default='Explore'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="metric_accuracy",
                    # Display name
                    name=bcolors.HEADER+" How important the metric 'Accuracy' is for you? 1-5: 1- Least important 5- Most Important"+bcolors.ENDC,
                    # Help message
                    help="Enter 1-5: 1 being least important, and 5 being most important",
                    validators=(wiz.required_validator),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="metric_speed",
                    # Display name
                    name=bcolors.HEADER+" How important the metric 'Speed' is for you? 1-5: 1- Least important 5- Most Important"+bcolors.ENDC,
                    # Help message
                    help="Enter 1-5: 1 being least important, and 5 being most important",
                    validators=(wiz.required_validator),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="metric_interpretability",
                    # Display name
                    name=bcolors.HEADER+" How important the metric 'Interpretability' is for you? 1-5: 1- Least important 5- Most Important"+bcolors.ENDC,
                    # Help message
                    help="Enter 1-5: 1 being least important, and 5 being most important",
                    validators=(wiz.required_validator),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="metric_implementation",
                    # Display name
                    name=bcolors.HEADER+" How important the metric 'Ease of Implementation and Maintenance' is for you? 1-5: 1- Least important 5- Most Important"+bcolors.ENDC,
                    # Help message
                    help="Enter 1-5: 1 being least important, and 5 being most important",
                    validators=(wiz.required_validator),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_column",
                    # Display name
                    name=bcolors.HEADER+" What does the data (columns) represent? well defined 'Features', 'signals' (Timeseries, pixels, etc) or Text - (Please type the associated number)"+bcolors.ENDC,
                    # Help message
                    help="1. Well Defined Features\n 2. Signals\n 3. Text - Unstructured\n 4. None of the above\n",
                    validators=(wiz.required_validator),
                    default='Features'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_signal_type",
                    # Display name
                    name=bcolors.HEADER+" If Signals, can you choose any one from the below list? "+bcolors.ENDC,
                    # Help message
                    help="1. Image\n 2. Audio\n 3. Timeseries\n 4. None of the above\n 5. Not Applicable\n  ",
                    validators=(wiz.required_validator),
                    default='3'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_text_type",
                    # Display name
                    name=bcolors.HEADER+" If Text, can you choose any one from the below list? "+bcolors.ENDC,
                    # Help message
                    help="1. Webpages\n 2. Emails\n 3. Social-Media Posts\n 4. Books\n 5. Formal Articles\n 6. Speech converted to text\n 7. None of the above\n 8. Not Applicable\n  ",
                    validators=(wiz.required_validator),
                    default='3'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_features",
                    # Display name
                    name=bcolors.HEADER+" If features, are they well defined? i.e., are all the variables well understood? "+bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_features_count",
                    # Display name
                    name=bcolors.HEADER+" If features, How many are there? "+bcolors.ENDC,
                    # Help message
                    help="Number or NA",
                    validators=(wiz.required_validator),
                    default='10'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_distribution",
                    # Display name
                    name=bcolors.HEADER+" Are you aware of any 'Distribution' that is inherent to the data, we can take advantage of?"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_io_relation",
                    # Display name
                    name=bcolors.HEADER+" Is the probability of 'Linear Relation' between input and the output is high?"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_correlation",
                    # Display name
                    name=bcolors.HEADER+" Are you confident that there is NO high correlation among the independent variables in your day?"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U. Change in one  ",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_cond_indep",
                    # Display name
                    name=bcolors.HEADER+" Are you confident that the variables are conditionally independent?"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U. If probability that it rains given lightining and thunder is same as probability that it rains given lightining, then rain and thunder are conditionally independent",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_missing",
                    # Display name
                    name=bcolors.HEADER+" Are there any missing values in the data? "+bcolors.ENDC,
                    # Help message
                    help="Y/N/U",
                    validators=(wiz.required_validator),
                    default='N'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_size_bytes",
                    # Display name
                    name=bcolors.HEADER+" How big is the data in terms of size? (Use K/M/G Bytes unit) "+bcolors.ENDC,
                    # Help message
                    help="Number(integer) and unit: K for Kilo, M for Mega and G for Giga. Ex: 10G for 10 Giga bytes",
                    validators=(wiz.required_validator),
                    default='1G'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_size_samples",
                    # Display name
                    name=bcolors.HEADER+" How big is the data in terms of samples? (Use T/M/B Samples) "+bcolors.ENDC,
                    # Help message
                    help="Number(integer) and unit: T for Thousand, M for Million and B for Billion. Ex: 1M for 1 Million Samples",
                    validators=(wiz.required_validator),
                    default='1M'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_type_output",
                    # Display name
                    name=bcolors.HEADER+" What is the expected output data type ? (Please type number associated with type in 'help') "+bcolors.ENDC,
                    # Help message
                    help=" 1:Numerical-Discrete\n 2:Numerical-Continuous\n 3:Ordinal\n 4:Categorical-Binary\n 5:Categorical-Multiclass",
                    validators=(wiz.required_validator),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_output_prob",
                    # Display name
                    name=bcolors.HEADER+" Is the expected output data a probability value ? "+bcolors.ENDC,
                    # Help message
                    help="Y/N",
                    validators=(wiz.required_validator),
                    default='N'
                ),
            )
        )


    def supervized_wizard(self):
        """
        The Supervized Learning Wizard
        """

    def unsupervized_wizard(self):
        """
        The Un-Supervized Learning Wizard
        """

    def reinforced_wizard(self):
        """
        The Reinforced Learning Wizard
        """
        message = """
            Reward  |--------|
            |-------| Agent  |  Action
            | |-----|        |-------|
            | |	    |--------|       |
            | |state                 |
            | |	                     |
            | |	   |-----------|     |
            | |----|Environment|     |
            |------|           |-----|
    	           |-----------|
            """
        self.wiz_reinforced = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Reinforcement Specific"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_info",
                    # Display name
                    name=bcolors.HEADER+" Type help for reference diagram for reinforcement-learning"+bcolors.ENDC,
                    # Help message
                    help=message,
                    validators=(wiz.required_validator),
                    default='Type Help or Press Enter'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_model_preference",
                    # Display name
                    name=bcolors.HEADER+" Do you prefer model-based approach? (Type NA if you are not sure) "+bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_model_availability",
                    # Display name
                    name=bcolors.HEADER+" Do you have a model for model-based approach? (Type NA if not applicable) "+bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_modelfree_value",
                    # Display name
                    name=bcolors.HEADER+" In Model-Free approach, do you prefer value-based approach? (Type NA if not applicable) "+bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_modelfree_value_state",
                    # Display name
                    name=bcolors.HEADER+" In Model-Free Value-Based approach, do you prefer state-only model? (Type NA if not applicable) "+bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
            )
        )

    ############### All the Run Operations ######################
    def run_mainwiz(self):
        """
        Run the Main Wizard
        """
        self.main_wizard_l1()
        self.main_l1_values = self.wiz_main_l1.run(self.shell)
        if self.main_l1_values['data_availability'].lower() == 'y':
            self.main_wizard_l2_b()
            self.main_l2b_values = self.wiz_main_l2_b.run(self.shell)
            if self.main_l2b_values['data_programmability'].lower() == 'y':
                print(bcolors.FAIL+"ML is not required - Please consider alternate approaches\n"+bcolors.ENDC)
            else:
                self.main_wizard_l3()
                self.main_l3_values = self.wiz_main_l3.run(self.shell)
                if self.main_l3_values['data_knowledge'].lower() == 'y':
                        print(bcolors.OKGREEN+"Looks like you need ML, let's continue"+bcolors.ENDC)
                else:
                    self.main_wizard_l4()
                    self.main_l4_values = self.wiz_main_l4.run(self.shell)
                    if self.main_l4_values['data_pattern'].lower() == 'y':
                        print(bcolors.OKGREEN+"Looks like you need ML, let's continue"+bcolors.ENDC)
                    else:
                        print(bcolors.FAIL+"ML is not required - Please consider alternate approaches\n"+bcolors.ENDC)
        else:
            self.main_wizard_l2_a()
            self.main_l2a_values = self.wiz_main_l2_a.run(self.shell)
            if self.main_l2a_values['data_creativity'].lower() == 'y':
                print(bcolors.OKGREEN+"Looks like you need ML, let's continue"+bcolors.ENDC)
            else:
                print(bcolors.FAIL+"ML is not required - Please consider alternate approaches\n"+bcolors.ENDC)
    
    def run_generic_wizard(self):
        """
        Run Generic Wizard
        """
        self.gen_wizard()
        self.gen_values = self.wiz_generic.run(self.shell)

    def run_learningtype_wizard(self):
        """
        Depending on the Main wizard values, run specific
        learning wizard
        """
    
    def run_unsupwiz(self):
        """
        Run UnSupervized Learning Wizard.
        """
    
    def run_reinforced_wizard(self):
        """
        Run Reinforced Learning Wizard
        """
        self.reinforced_wizard()
        self.ri_values = self.wiz_reinforced.run(self.shell)


    def decide_reinforced(self):
        """
        Decide which reinforement learning to use.
        """
        if int(self.gen_values['data_type_output']) == 2:
            if ('y' in ri_values['ri_model_preference'].tolower():
                    'y' in ri_values['ri_model_availability'].tolower()):
                print("Start with Reinforcement Learning - AlphaZero")
            else:
                print("Reinforcement Learning models to consider - World Models, I2A, MBMF, and MBVE")
        else:
            if 'y' in ri_values['ri_model_preference'].tolower():
                print("Reinforcement Learning models to consider - World Models, I2A, MBMF, and MBVE")
            else:
                # Model-Free based approach.
                if 'y' not in ri_values['ri_modelfree_value'].tolower():
                    print("Reinforcement Learning models to consider: Policy Gradient and Actor Critic")
                else:
                    if 'y' in ri_value['ri_modelfree_value_state'].tolower():
                        print("Reinforcement Learning models to consider - Monte Carlo, TD(0), and TD(Lambda)")
                    else:
                        print("Reinforcement Learning models to consider - SARSA, QLearning, Deep Queue Nets")


    def decide_supervised(self):
        """
        Decide which Supervized learning to use.
        """
        # Decide whether data is Low or High
        data_size = 'unknown'
        if ('k' in self.gen_values['data_size_bytes'].lower() or
                't' in self.get_values['data_size_samples']):
            data_size = 'low'
        else:
            data_size = 'high'

        if int(self.gen_values['metric_interpretability']) >= 3 :
            interpretability = True
        else:
            interpretability = False
        
        if int(self.gen_values['metric_speed']) >= 3 :
            faster = True
        else:
            faster = False
            

        # Decide Features relative to Data (ftod_ratio) - high/low
        if ('k' in self.gen_values['data_size_bytes'].lower() or 
                't' in self.gen_values['data_size_samples']):
            if int(gen_values['data_features_count']) > 50:
                ftod_ratio = 'high'
            else:
                ftod_ratio = 'low'
        elif ('m' in self.gen_values['data_size_bytes'].lower() or 
                'm' in self.gen_values['data_size_samples']):
            if int(gen_values['data_features_count']) > 5000:
                ftod_ratio = 'high'
            else:
                ftod_ratio = 'low'
        else:
            if int(self.gen_values['data_features_count']) > 500000:
                ftod_ratio = 'high'
            else:
                ftod_ratio = 'low'
        
        if 'high' in data_size:
            # Cover: DT, RF, RNN, CNN, ANN and Naive Bayes
            if interpretability:
                if faster:
                    print("Start with Supervised Learning - Decision Tree")
                    return
                else:
                    print("Start with Supervised Learning - Random Forest")
                    return
            else:
                if int(self.gen_values['data_column']) == 3:
                    print("Start with Supervised Learning - RNN")
                elif (int(self.gen_values['data_column']) == 2 and
                        int(self.gen_values['data_signal_type']) == 1):
                        print("Start with Supervised Learning - CNN")
                elif (int(self.gen_values['data_column']) == 2 and
                        (int(self.gen_values['data_signal_type']) == 2 or
                            int(self.gen_values['data_signal_type']) == 3)):
                        if 'y' in gen_values['data_output_prob'].tolower():
                            print("Start with Supervised Learning - Naive Bayes")
                        else:
                            print("Start with Supervised Learning - ANN")
                else:
                    print("Start with Supervised Learning - ANN")
        else:
            from_b = False
            # Cover: Regressions
            if 'low' in ftod_ratio:
                print("Start with Supervised Learning - SVN with Gaussian Kernel")
            else:
                from_b = True


            if int(self.gen_values['data_type_output']) == 2:
                if 'y' in self.gen_values['data_io_relation'].tolower():
                    print("Start with Supervised Learning - Linear Regression or Linear SVM")
                else:
                    print("Start with Supervised Learning - Polynomial Regression or nonLinear SVM")
            else:
                from_b = True
            if from_b:
                if int(self.gen_values['data_output_type']) == 4:
                    if 'y' in self.gen_values['data_output_prob'].tolower():
                        if 'y' in self.gen_values['data_cond_indep'].tolower():
                            print("Start with Supervised Learning - Naive Bayes")
                        else:
                            if 'y' in self.gen_values['data_correlation'].tolower():
                                print("Start with Supervised Learning - LASSO or Ridge Regression")
                            else:
                                print("Start with Supervised Learning - Logistic Regression")
                    else:
                        print("Start with Supervised Learning - Polynomial Regression or nonLinear SVM")

                else:
                    print("Start with Supervised Learning - KNN")




def signal_handler(signum, frame):
    """
    Signal Handler
    """
    print("\n You interrupted, No Suggestion will be provided!")
    print(signum, frame)
    sys.exit(0)

def main():
    """
    The Main Function
    """
    try:
        algowiz = AlgoSelectorWizard()
#        algowiz.run_mainwiz()
#        algowiz.run_generic_wizard()
        algowiz.run_reinforced_wizard()
    except(KeyboardInterrupt, MemoryError):
        print("Some Error Occured - No Suggestion can be provided")

    print("Thanks for using the Algoselector-Wizard, " +
            "Hope our suggestion will be useful")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    message = """
        Reward  |--------|
        |-------| Agent  |  Action
        | |-----|        |-------|
        | |     |--------|       |
        | |                      |
        | |state                 |
        | |                      |
        | |    |-----------|     |
        | |----|Environment|     |
        |------|           |-----|
               |-----------|
        """
    main()
