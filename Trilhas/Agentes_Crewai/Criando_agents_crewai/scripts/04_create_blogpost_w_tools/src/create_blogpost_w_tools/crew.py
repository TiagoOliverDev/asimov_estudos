from dotenv import load_dotenv

_ = load_dotenv()

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool

import agentops
agentops.init()

serper = SerperDevTool()
scraper = ScrapeWebsiteTool()
file_write = FileWriterTool()

@CrewBase
class CreateBlogpostWTools():
	"""CreateBlogpostWTools crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def pesquisador_de_conteudo(self) -> Agent:
		return Agent(
			config=self.agents_config['pesquisador_de_conteudo'],
			tools=[serper],
			verbose=True
		)

	@agent
	def planejador_de_conteudo(self) -> Agent:
		return Agent(
			config=self.agents_config['planejador_de_conteudo'],
			tools=[scraper],
			verbose=True
		)

	@agent
	def escritor_do_blog(self) -> Agent:
		return Agent(
			config=self.agents_config['escritor_do_blog'],
			verbose=True
		)

	@agent
	def revisor_do_conteudo(self) -> Agent:
		return Agent(
			config=self.agents_config['revisor_do_conteudo'],
			verbose=True
		)

	@task
	def pesquisa_conteudo(self) -> Task:
		return Task(
			config=self.tasks_config['pesquisa_conteudo'],
		)

	@task
	def planejamento_conteudo(self) -> Task:
		return Task(
			config=self.tasks_config['planejamento_conteudo'],
		)

	@task
	def escrita_blog_post(self) -> Task:
		return Task(
			config=self.tasks_config['escrita_blog_post'],
		)

	@task
	def revisao_conteudo(self) -> Task:
		return Task(
			config=self.tasks_config['revisao_conteudo'],
		)

	@task
	def salva_conteudo(self) -> Task:
		return Task(
			config=self.tasks_config['salva_conteudo'],
			tools=[file_write]
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the CreateBlogpostWTools crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
