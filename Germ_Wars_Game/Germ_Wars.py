import os
import sys
import time
import random

# Germ Wars Project by Whit Blodgett
#######################################################
def typewriter(text,delay = 0.02):
    '''animated printing method'''
    for i in (text):
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(delay)
class Game():
    '''Main game engine'''
    def __init__(self):
        '''Starting conditions for germ wars'''
        self.turn = 0
        self.initial_infection = random.choice([4,6,10,12,14,16])
    def help_menu(self):
        print('Welcome to Germ Wars\n')
        print('The goal of the game is to alot your production points to\nbattling the virus by building hospitals and researching a cure. \n\nVirus: This is a spontaneous, unruly character that will emerge in a \nrandom sample of your population and grow according to your population density (pre-set)')
        print('Hospitals: Built by alotting production points, these cure 1 case per turn')
        print('Vaccines: Researching a vaccines isn\'t a sure thing but if you alot points,\nyou could very well discover one and win!')
        wait = input("Press [Enter] to continue.")
        self.menu()
    def timestep(self):
        '''each turn'''
        self.turn +=1
        for i in self.people:
            i.timestep()
    # bring your population to the hospital to cure as many as you can! 
        self.visit_hospital(self.economy.hospitals,self.people) 
        self.cured_cases = self.economy.hospitals
    # returns a number of new cases determined by the Virus Class
        self.cases = self.virus.new_cases(self.cases) - self.cured_cases
    # check to see if vaccine was discovered
        self.found_cure()
    # infect the population by the num of new cases that turn
        for i in range(self.cases):
            self.people[i].infect()
    # print visual of sick people           
        # print(self.people)
    # check to see if everyone is cured
        # create list of health statuses
        health_check = []
        for i in self.people:
            health_check.append(i.health)
        for i in health_check:
            if  i == "infected":
                break
            else:
                print('Everyone is cured! You win! Great work!')
                quit()
        self.menu()
    def visit_hospital(self,hospitals,people):
        '''cures 1 case per hospital per turn'''
        self.counter = hospitals
        self.people = people
        for i in self.people:
            if i.health == "infected":
                i.heal()
                self.counter -= 1
                if self.counter == 0:
                    break
                else:
                    continue
            else:
                continue  
    def found_cure(self):
        '''based on chance and difficulty, determines how many research_points to find cure & tests if you hit them'''
        self.research_needed = random.choice([60,70,80,90,100])
        if self.economy.vaccine_research > self.research_needed:
            print('You found a Vaccine! Your entire population has been healed \nand you have won the game! Well done!')
            quit()
    def menu(self):
        '''core menu for each day'''
        os.system('clear')
        typewriter('##############################################\n----PROCESSING--->\n##############################################',.01)
        os.system('clear')
        for i in self.people:
            if i.health == 'infected':
                x = ('X ')
                typewriter(x,.003)
        print('\nDay: ',self.turn)
        print("{} cases today. \nAbout {:.1%} of your people are sick.".format(self.cases, (self.cases/self.population)))
        print("Virus Aggression: {}".format(self.difficulty))
        if self.turn == 0:
            pass
        else:
            print('You cured:', self.cured_cases, 'cases last turn!')
        print('##############################################')
        # print("Production Points Left: " + str(self.economy.production_points))
        print("Points dedicated to vaccine research: " + str(self.economy.vaccine_research))
        print("Hospitals Built: " + str(self.economy.hospitals))
        
        moptions = '''
        ##############################################
        | Pick an option                             |
        | 1) Advance Turn                            |
        | 2) Allot Resources                         |
        | 3) Restart                                 |
        | 4) Help                                    |
        | 5) Quit                                    |
        ##############################################
        '''
        print(moptions)
        options = {"1":self.timestep, "2":self.choice_menu, "3":self.runGame, "4":self.help_menu } 
        while True:
            pick = input('Pick an Option... ')
            os.system('clear')
            if pick == "5":
                quit()
            elif pick in options.keys():
                 break
            else:
                print('Please try again')
                continue
        # print(self.continent.density)
        try:
            options[pick]()
        except IndexError:
            print('Everyone got the virus! Please try again! ')
    def choice_menu(self):
        '''default menu'''
        os.system('clear')
        # print("Production Points Left: " + str(self.economy.production_points))
        print("Points dedicated to vaccine research: " + str(self.economy.vaccine_research))
        print("Hospitals Built: " + str(self.economy.hospitals))
        print("{} people are infected out of {} people,  \nVirus Aggression: {}".format(self.cases, self.population,self.difficulty))
        moptions2 = '''
        ##############################################
        | Choose an option                           |
        | 1) Research a Vaccine                      |
        | 2) Build Hospitals                         |
        ##############################################
        '''
        print(moptions2)
        options2 = {"1":self.vaccine_allot,"2":self.hospital_allot} 
        while True:
            pick2 = input('Pick an Option... ')
            if pick2 in options2.keys():
                break
            else:
                print('Please try again')
                continue
        options2[pick2]()
    def vaccine_allot(self):
        '''allows player to research vaccine'''
        os.system('clear')
        # print("Production Points Left: " + str(self.economy.production_points))
        print("Points dedicated to vaccine research: " + str(self.economy.vaccine_research))
        moptions3 = '''
        ##############################################
        | Choose how many points to allot to         |
        | reasearching a vaccine                     |
        | 1) 5 points                                |
        | 2) 10 points                               |
        | 3) 20 points                               |
        | 4) 50 points                               |
        |                                            |
        | (PS: can't win until you find a vaccine!)  |
        ##############################################
        '''
        print(moptions3)
        # self.economy.research_vaccine(5)
        pick3 = input('Pick an Option... ')
        if pick3 == '1':
            self.economy.research_vaccine(5)
        elif pick3 == '2':
            self.economy.research_vaccine(10)
        elif pick3 == '3':
            self.economy.research_vaccine(20)
        elif pick3 == '4':
            self.economy.research_vaccine(50)
        else:
            print('Please try again')
        self.timestep()
    def hospital_allot(self):
        '''allows player to build hospitals'''
        os.system('clear')
        # print("Production Points Left: " + str(self.economy.production_points))
        print("Hospitals Built: " + str(self.economy.hospitals))
        moptions4 = '''
        ##############################################
        | How many hospitals do you want to build?   |
        | 1) 5 hospitals                             |
        | 2) 10 hospitals                            |
        | 3) 20 hospitals                            |
        | 4) 50 hospitals                            |
        |                                            |
        | (PS: 1 hospitals heals 1 person per turn!) |
        ##############################################
        '''
        print(moptions4)
        pick4 = input('Pick an Option... ')
        if pick4 == '1':
            self.economy.build_hospital(5)
        elif pick4 == '2':
            self.economy.build_hospital(10)
        elif pick4 == '3':
            self.economy.build_hospital(20)
        elif pick4 == '4':
            self.economy.build_hospital(50)
        else:
            print('Please try again')
        self.timestep()
    def runGame(self):
        '''runs the game'''
        os.system('clear')
        print("------------GERM WARS------------\n")  
        print('"I expect countries will participate \nin regular “germ games” in the same \nway as armed forces take part in \nwar games."\n\n-Bill Gates 2020')
        print()
        wait = input("Press [Enter] to play.")
        os.system('clear')
        '''Run the game engine - loops until game is complete'''
        day = 0
        print('Outbreak! As part of an effort to defend the world, you must lead a continent \nin it\'s battle against a simulated virus')
        # ideal spot for an overview of the continents 
        choice = 'North America' # input('Choose a Continent ')
        self.difficulty = input('Choose a Virus Aggression\n[1] Easy\n[2] Medium\n[3] Hard\n')
        self.continent = Continent(choice, happiness = 10)
        self.economy = Economy(self.continent.productivity_x)
        self.population = self.continent.population
        self.virus = Virus(self.continent.density, self.population, self.difficulty) #  strain_aggression==self.difficulty
        self.default()
        self.menu()
    def default(self):
        '''creates a dictionary of individual Person objects and infects an initial amount of them'''
        self.people = [Person() for i in range(self.population)]
        # self.people = {i:(Person()) for i in range(self.population)}
        self.cases = 0
        for i in range(self.initial_infection):
            self.people[i].infect()
            self.cases += 1
#######################################################
class Continent():

    def __init__(self, choice, happiness):
        self.happiness = happiness
        self.choice = choice
        # REDUCE count by turning this into CSV upload 
        if self.choice == "North America":
            self.population = 579
            self.size = 10
            self.productivity_x = 10
        elif self.choice == "Asia":
            self.population = 4463
            self.size = 18
            self.productivity_x = 10
        elif self.choice == "Europe":
            self.population = 742
            self.size = 4
            self.productivity_x = 9
        elif self.choice == "Australia":
            self.population = 24
            self.size = 3
            self.productivity_x = 7
        elif self.choice == "South America":
            self.population = 423
            self.size = 7
            self.productivity_x = 5
        elif self.choice == "Africa":
            self.population = 1200
            self.size = 12
            self.productivity_x = 3
        else:
            print('Try again')
        self.density = (self.population)//(self.size)
    # def close_border(self):
        '''Increases unhapiness, decreases spread 
        rate if continents level of virus is low enough. 
        Otherwise has no effect on spread. '''
#######################################################
class Economy():
    '''This class represents the continents productivity
    as measured by production points'''
    def __init__(self, productivity_x): 
        self.productivity_x = productivity_x
        self.production_points = int(self.productivity_x * 10)
        self.vaccine_research = 0
        self.hospitals = 0
    def timestep(self):
        '''produces additional points based on healthy pop'''
        # return self.production_points
        # per turn generated, how does this work with timestep? 
    # def timestep(self, healthy_people):
        # self.productivity_points = healthy_people * 
    def research_vaccine(self, alotted_vac_points):
        '''researches vaccine with alotted points'''
        self.alotted_vac_points = alotted_vac_points
        self.vaccine_research += self.alotted_vac_points
        # self.production_points -= self.alotted_vac_points
        
    def build_hospital(self, alotted_hos_points):
        '''builds hospitals with alotted points'''
        self.alotted_hos_points = alotted_hos_points
        self.hospitals += self.alotted_hos_points
        # self.production_points -= self.alotted_hos_points
    # def educate(self, productivity_points):
    #     pass
    # def make_masks(self, productivity_points):
    #     pass
#######################################################
class Person():
    def __init__(self):
        self.health = "clear"
        # self.sick_days = 0
    def timestep(self):
        pass
    #     # if self.sick_days > 0:
    #     #     self.sick_days -=1
    #     # else:
    #     #     self.health = "clear"
    def __repr__(self):
        if self.health == "clear":
            return "{}".format(self.health)
        else:
            return "{}".format(self.health)# self.sick_days  ##, healthy in {} day(s)
    @classmethod
    def Count(cls):
        return cls.count

    def infect(self):
        '''infects the person with the virus'''
        self.health = "infected"
        # self.sick_days = 14

    def heal(self):
        '''heals the person from the virus'''
        self.health = "clear"     
#######################################################
class Virus():
    '''takes in the infected count and outputs the new number of infected'''
    def __init__(self, density, population, difficulty):
        self.density = density # count US is 57
        # self.sick_count = sick_count # count 
        self.population = population 
        # self.initial_infection = infected_count
        self.difficulty = int(difficulty)
        # self.masks = masks # count
        # self.education = education # count
    # def __repr__(self):
    #     return "{} people are infected out of {} people,  \nVirus Aggression: {}".format(self.infected_count, self.population,self.difficulty)
    
    def new_cases(self, infected_count):
        '''takes in current infected count and outputs new infected number'''
        # self.infected_count = infected_count
        self.infected_count = infected_count
        # self.cured_cases = cured_cases
        if infected_count >= 2:
            self.new_infected_count = 1+int(infected_count + (infected_count//3)*(self.difficulty * self.density // 10))
        else:
            self.new_infected_count = int((infected_count) + (infected_count//3)*(self.difficulty * self.density // 10))
        return self.new_infected_count
#######################################################
game = Game()
game.runGame()