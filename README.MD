 WikiBlog – Project Documentation 

1. Overview 

WikiBlog is a simple terminal-based assistant that pulls information from Wikipedia based on user input. 

 It greets the user according to the current time, accepts prompts, fetches summaries or detailed articles, prints them word-by-word with a typing effect, and then offers related topics for deeper exploration. 

The program runs in a loop until the user types quit. 

 

2. Features 

Time-based greeting 

The script detects the current hour and greets the user accordingly. 

Wikipedia search 

    Uses wikipedia.search() to find topics. 

    Picks the top match automatically. 

    Handles missing pages and disambiguation. 

 Full content 

If the user includes the word detail or detailed, the script fetches the full article. 

 Otherwise, it fetches a summary. 

Typing-effect output 

Each word is printed with a small delay using time.sleep(). 

Topic explorer 

After the main summary, the program: 

    Lists all related topics from the search. 

    Lets the user pick one by entering a number. 

    Fetches and prints its summary. 

Graceful exit options 

    Enter quit anywhere to exit. 

    Enter break in topic mode to start a new query. 

    Keyboard interrupts are handled cleanly. 

 

3. Requirements 

Python version 

Python 3.8 or later recommended. 

Packages 

Install using pip inside your virtual environment: 

pip install wikipedia 
  

Virtual environment setup 

source ~/myenv/bin/activate 
  

4. Project Structure 

WikiBlog/ 
│ 
├── wikiblog.py      # Main program file 
└── README.md        # Documentation 
  

5. Code Walkthrough 

greet() 

    Asks for the user’s name. 

    Checks current hour using datetime.now().hour. 

    Prints a greeting based on time ranges: 

    Morning (5–11) 

    Afternoon (12–15) 

    Evening (15–19) 

    Default greeting for late night 

 

prompting() 

This is the main loop of the program. 

Input handling 

    Reads user’s prompt. 

    Exits if the user types quit. 

Wikipedia search 

topics = wikipedia.search(prompt) 
res = topics[0] 
  

If the prompt includes “detail” or “detailed”, full content is retrieved. Otherwise, a summary is shown. 

Output typing effect 

Words are printed one at a time: 

print(word, end=' ', flush=True) 
time.sleep(0.1) 
  

Error handling 

    PageError: Page not found. 

    DisambiguationError: Prompt is unclear; user sees options. 

 

Topic Exploration Sub-loop 

After showing the main answer: 

    Lists related topics. 

    Asks the user to choose one. 

    Fetches and prints its summary. 

Special commands: 

    quit → exit script 

    break → return to main prompt 

 

6. Example Run 

welcome back to WikiBlog! 
Enter your name: renuka 
Good Evening Renuka! How are you doing today? 
 
Enter your message: python 
Generating your prompt. This may Take a while... 
 
Here is what I found about python 
Python is an interpreted high-level programming... 
  

Then related topics appear with numbers for selection. 

 

7. Future Improvements (Optional) 

    Add colored terminal output. 

    Add logging for errors. 

    Cache queries to avoid repeated API calls. 

    Display headings instead of only printing raw text. 

    Add text-to-speech for summaries. 

 

8. Conclusion 

WikiBlog offers a simple interactive way to fetch and explore Wikipedia content. 

 It combines user prompts, time-based greetings, Wikipedia search, and dynamic output formatting to create a lightweight terminal assistant. 

 

 

 

9.Output 
Output Image

 