from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class CreateCrews():
    """CreateCrews crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researarquiteto_de_solucaocher(self) -> Agent:
        return Agent(
            config=self.agents_config['arquiteto_de_solucao'], # type: ignore[index]
            verbose=True
        )

    @agent
    def especialista_em_agentes(self) -> Agent:
        return Agent(
            config=self.agents_config['especialista_em_agentes'], # type: ignore[index]
            verbose=True
        )
    

    @agent
    def gerente_de_fluxo_de_trabalho(self) -> Agent:
        return Agent(
            config=self.agents_config['gerente_de_fluxo_de_trabalho'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def engenheiro_de_orquestracao(self) -> Agent:
        return Agent(
            config=self.agents_config['engenheiro_de_orquestracao'], # type: ignore[index]
            verbose=True
        )


    @task
    def planejar_arquitetura_do_sistema(self) -> Task:
        return Task(
            config=self.tasks_config['planejar_arquitetura_do_sistema'], # type: ignore[index]
            output_file='report.md'
        )
    
    @task
    def criar_os_agentes(self) -> Task:
        return Task(
            config=self.tasks_config['criar_os_agentes'], # type: ignore[index]
        )
    
    @task
    def definir_as_tarefas(self) -> Task:
        return Task(
            config=self.tasks_config['definir_as_tarefas'], # type: ignore[index]
        )
    
    @task
    def desenvolver_o_arquivo_de_orquestracao(self) -> Task:
        return Task(
            config=self.tasks_config['desenvolver_o_arquivo_de_orquestracao'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
