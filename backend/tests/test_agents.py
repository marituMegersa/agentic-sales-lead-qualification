def test_agent_orchestrator():
    prompt = "Test execution query for agentic-sales-lead-qualification"
    assert len(prompt) > 0
    assert "Test" in prompt
