nest_asyncio.apply()
model=LiteLLMModel(
    model_id="openai/gpt-4o-mini",

)
async def run_hospital_workflow() :

    async with Client(base_url="http://localhost:8001") as insurer, Client(base_url:'xxxx') as hospital:
         agent_collection=await AgentCollention.from_acp(insurer, hospital)
         acp_agents={agent.name:{'agent':agent,'client':client} for agent, client in agent_collection.items()}
         acpagent=ACPCallingAgent(acp_agentss=acp_agents,model=model)
         result=await acpagent.run("sadsdads")
asyncio.run(run_hospital_workflow())
