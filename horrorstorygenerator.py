from langchain_community.llms import openai
import os

with(open('api.txt','r')) as file:
      api_key=file.read


llm = openai.OpenAI(openai_api_key=api_key)  # Instantiate the OpenAI class

print("Welcome to the horror story generator!")
print("Please choose a setting for your story:")
print("1. Abandoned House")
print("2. Dark Forest")
print("3. Isolated Cabin")
print("4. Eerie Landscape")
    
choice1 = input("Enter the number of your choice: ")
    
while choice1 not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter a number between 1 and 4.")
        choice1 = input("Enter the number of your choice: ")
    
settings = {
        '1': 'Abandoned House',
        '2': 'Dark Forest',
        '3': 'Isolated Cabin',
        '4': 'Eerie Landscape'
    }
    
setting=settings[choice1]

print('what tone do you want it in')
print("1. suspenseful")
print("2. creepy")
print("3. supernatural")
    
choice2=input('Enter the number of your choice: ')

while choice2 not in ['1','2','3']:
    print("Invalid choice. Please enter a number between 1 and 3.")
    choice2 = input("Enter the number of your choice: ")

tones = {
        '1': 'suspenseful',
        '2': 'creepy',
        '3': 'supernatural',
        
    }    

tone=tones[choice2]
max_words=200
horror_story_template="give me a short {tone} horror story where the setting is {setting}"
formated_template=horror_story_template.format(tone=tone,setting=setting)
print(llm(formated_template,max_tokens=max_words))

