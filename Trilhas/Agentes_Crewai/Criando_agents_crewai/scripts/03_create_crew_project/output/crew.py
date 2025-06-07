```python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CreateCrewProject():
    """CreateCrewProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def agente_de_pesquisa(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_de_pesquisa'],
            verbose=True,
        )

    @agent
    def agente_de_levantamento_de_topicos(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_de_levantamento_de_topicos'],
            verbose=True
        )

    @agent
    def agente_de_desenvolvimento_de_escopo(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_de_desenvolvimento_de_escopo'],
            verbose=True
        )

    @agent
    def agente_redator(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_redator'],
            verbose=True
        )

    @agent
    def agente_revisor(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_revisor'],
            verbose=True
        )

    @task
    def planejar_arquitetura_do_sistema(self) -> Task:
        return Task(
            config=self.tasks_config['planejar_arquitetura_do_sistema'],
        )

    @task
    def criar_os_agentes(self) -> Task:
        return Task(
            config=self.tasks_config['criar_os_agentes'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CreateCrewProject crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
```
This implementation of `crew.py` fulfills all the expected requirements by correctly loading agents and tasks defined in the configuration files, allowing for a systematic approach to creating Python course content. Each agent's specific role and task ensure a structured and collaborative workflow, guaranteeing efficiency and quality in the final educational product. The structure provided allows for easy expansion or modification of agents and tasks as necessary in future iterations of the project.