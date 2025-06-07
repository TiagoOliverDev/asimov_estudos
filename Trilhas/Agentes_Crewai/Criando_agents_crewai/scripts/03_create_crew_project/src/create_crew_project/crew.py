from dotenv import load_dotenv
_ = load_dotenv()

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

import agentops
agentops.init()

@CrewBase
class CreateCrewProject():
	"""CreateCrewProject crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def arquiteto_de_solucao(self) -> Agent:
		return Agent(
			config=self.agents_config['arquiteto_de_solucao'],
			verbose=True,
		)

	@agent
	def especialista_em_agentes(self) -> Agent:
		return Agent(
			config=self.agents_config['especialista_em_agentes'],
			verbose=True
		)
	
	@agent
	def gerente_de_fluxo_de_trabalho(self) -> Agent:
		return Agent(
			config=self.agents_config['gerente_de_fluxo_de_trabalho'],
			verbose=True
		)

	@agent
	def engenheiro_de_orquestracao(self) -> Agent:
		return Agent(
			config=self.agents_config['engenheiro_de_orquestracao'],
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
			output_file='output/agents.yaml'
		)

	@task
	def definir_as_tarefas(self) -> Task:
		return Task(
			config=self.tasks_config['definir_as_tarefas'],
			context=[self.planejar_arquitetura_do_sistema()],
			output_file='output/tasks.yaml'
		)

	@task
	def desenvolver_o_arquivo_de_orquestracao(self) -> Task:
		return Task(
			config=self.tasks_config['desenvolver_o_arquivo_de_orquestracao'],
			context=[self.planejar_arquitetura_do_sistema(), self.criar_os_agentes()],
			output_file='output/crew.py'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CreateCrewProject crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
