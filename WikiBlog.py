import wikipedia     #run this in virtual env:  source ~/myenv/bin/activate
import sys 
import time 
from datetime import datetime  #Timely greetings

def greet():
    print("Welcome back to WikiBlog!")
    name = input("Enter your name: ")
    time1 = datetime.now().hour

    if 5 <= time1 <= 11:
        print(f"Good Morning {name.capitalize()}! What do you want to talk about today?")   #name.capitalize() will capitalize the name
    elif 12 <= time1 <= 15:
        print(f"Good Afternoon {name.capitalize()}! What's new?")
    elif 15 <= time1 <= 19:
        print(f"Good Evening {name.capitalize()}! How are you doing today?")
    else:
        print(f"Hello {name.capitalize()}! What's up?")

def prompting():      #this function is for the message that you give
    while True:
        prompt = input("Enter your message: ")

        if prompt.lower() == "quit":
            print("Goodbye for now!See you next time.")
            sys.exit()

        try:
            topics = wikipedia.search(prompt)        #The wikipedia.search(prompt) will return a list of topics
            res = topics[0]        #We will choose the first list element to generate a para

            print("\n Generating your prompt.This may Take a while...")

            if "detailed" in prompt.lower() or "detail" in prompt.lower():
                page = wikipedia.page(res)    #wikipedia.page() will return the entire page 
                content = page.content
                print(f"\n Here is what I found about {prompt}")
                words1 = content.split()
            else:
                summary = wikipedia.summary(res)
                print(f"\nHere is what I found about {prompt}")
                words1 = summary.split()

            try:
                for word in words1:
                    print(word, end=' ', flush=True)   #flush=True is used to generate output with a delay of 0.1sec
                    time.sleep(0.1)
                print()
            except KeyboardInterrupt:        #Even if there's any keyboard interrupt ctrl+c the program shouldn't stop
                print("\nInterrupted. You can enter a new message.") 
                continue

        except wikipedia.exceptions.PageError:     #Even if there is no content in the wikipedia page it should still continue
            print("Couldn't find summary on that topic")
            continue

        except wikipedia.exceptions.DisambiguationError as e:   #if you didnt give the prompt right
            print("Give some other input. The input is not valid.")
            print(e.options)
            continue

        time.sleep(2)

        # ================= TOPIC SECTION =================
        while True:       #after generating list[0] we will be showing list of other topics to view
            j = 0
            print("\nDo you want me to generate para to the related topics?")
            time.sleep(2)

            for topic in topics:
                print(f"{j}.{topic}")
                j = j + 1

            print("\n")

            ch = input("Enter the topic number you want to go through(quit to exit and break to start a new convo)")
            print("\n")

            if ch.lower() == "quit":
                print("Goodbye for now!See you later.")
                sys.exit()

            elif ch.lower() == "break":
                break

            elif ch.isdigit():
                index = int(ch)
                if 0 <= index <= len(topics):
                    print("Generating..This may take a while....")

                    try:
                        res1 = wikipedia.summary(topics[index], auto_suggest=True)

                    except wikipedia.exceptions.PageError:
                        print(f"Couldn't find results for the topic: {topics[index]}")
                        continue

                    except wikipedia.exceptions.DisambiguationError as e:
                        print("Topic is ambiguous. Choose another:")
                        print(e.options)
                        continue

                    except KeyboardInterrupt:
                        print("\nInterrupted.You can enter a new message.")
                        continue

                    words2 = res1.split()

                    try:
                        for w2 in words2:
                            print(w2, end=' ', flush=True)
                            time.sleep(0.1)
                        print()
                    except KeyboardInterrupt:
                        print("\nInterrupted. You can enter a new message.")
                        continue

            else:
                print("Give the correct number of the topic")

greet()
prompting()


This is wikiblog 2 with some features(say) 
These lines are to understand purely branch merge

Now to merge using remote repo