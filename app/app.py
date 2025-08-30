# Main application file for Deep Agents
from tools.tavily import get_tavily_client
from deepagents import create_deep_agent, SubAgent
from prompts.prompts import sub_research_prompt, sub_critique_prompt, research_instructions
from tools.tavily import internet_search
from utils.llms import fast_model
from dotenv import load_dotenv
load_dotenv()
tavily_client = get_tavily_client()




# Create the sub agents
research_sub_agent = {
    "name": "research-agent",
    "description": "Used to research more in depth questions. Only give this researcher one topic at a time. Do not pass multiple sub questions to this researcher. Instead, you should break down a large topic into the necessary components, and then call multiple research agents in parallel, one for each sub question.",
    "prompt": sub_research_prompt,
    "tools": ["internet_search"],
}

critique_sub_agent = {
    "name": "critique-agent",
    "description": "Used to critique the final report. Give this agent some information about how you want it to critique the report.",
    "prompt": sub_critique_prompt,
}



# Create the the main agent
agent = create_deep_agent(
    tools=[internet_search],
    model= fast_model,
    instructions= research_instructions,
    subagents=[critique_sub_agent, research_sub_agent],
).with_config({"recursion_limit": 25})




## We can use langgraph cli to run the agent
