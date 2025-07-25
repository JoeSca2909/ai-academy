from crewai import Agent, Task, Crew
from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool, WebsiteSearchTool

dir_tool = DirectoryReadTool(directory="./Giorno_6")
file_tool = FileReadTool()

files = ["./Giorno_6/Mail.txt", "./Giorno_6/nota_di_credito.txt", "./Giorno_6/Fattura.txt"]

# Definizione dell’agente Planner CrewAI
planner = Agent(
    type="planner",
    name="Anonimizzatore",
    role="Anonimizza documenti",
    goal="Identificare i dati sensibili tipo IBAN, email, nome e cognome nei documenti e sostituirli con un placeholder",
    backstory="Esperto nella protezione dei dati personali, specializzato nell'anonimizzazione di documenti aziendali.",
    tools=[dir_tool, file_tool]
)

task_planner = Task(
    agent=planner,
    description="Apri i file nella cartella specificata e identifica i dati sensibili da anonimizzare",
    expected_output="Documenti anonimizzati"
)

crew = Crew(
    agents=[planner],
    tasks=[task_planner]
)

result = crew.kickoff()
print(result)