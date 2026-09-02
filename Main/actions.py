import os
import psutil
import time
import asyncio
import os


#============================================================#
#--------------------MONITORING-FEATURE----------------------#
#============================================================#
 
def agent_view():
    distractions = ["msedge.exe", "chrome.exe", "whatsapp.exe"]
    
    try:
        for process in psutil.process_iter(['name']):
            if process.info["name"] in distractions:

# 'w' mode creates the file if it doesn't exist

                with open("eyes.txt", 'w', encoding="utf-8") as f:
                    f.write(process.info['name'])
                return True
            
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass 

# Check idle state
    if psutil.cpu_percent(interval=1) < 5:
        return True
        
    return False






#============================================================#
#-----------------------ACTIONS-FEATURE----------------------#
#============================================================#

async def agent_actions():

    value=agent_view()

    if value:
        if os.path.exists("eyes.txt"):
            with open("eyes.txt", "r", encoding="utf-8") as f:
                target_name = f.read().strip()
            
# Kill the process using psutil instead of os.system
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] == target_name:
                    try:
                        proc.terminate()
                    except psutil.NoSuchProcess:
                        pass
            
            time.sleep(2)
            if os.path.exists("eyes.txt"):
                os.remove("eyes.txt")
                
    elif not value:
        with open("ears.txt","w",encoding="utf-8") as f:
            f.write("")







#============================================================#
#-----------------------TALKING-FEATURE----------------------#
#============================================================#

#async def Mevak():

    #doc=nlp(user.lower())
    #lemas= [token.lemma_ for token in doc]
    #with open("ask.txt", "w", encoding="utf-8") as f:
    #        f.write(" ".join(lemas))






async def main_loop():
    while not os.path.exists("ears.txt"):
        
        await agent_actions()
# Prevent high CPU usage from the loop itself
        await asyncio.sleep(1)






if __name__ == "__main__":
    asyncio.run(main_loop())

  #      asyncio.run(Mevak())
   #     if os.path.exists("ask.txt"):
    #        os.remove("ears.txt")
