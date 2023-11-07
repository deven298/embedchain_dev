from embedchain.memory.message import BaseMessage, ChatMessage


def test_ec_base_message():
    content = "Hello, how are you?"
    by = "human"
    metadata = {"key": "value"}

    message = BaseMessage(content=content, by=by, metadata=metadata)

    assert message.content == content
    assert message.by == by
    assert message.metadata == metadata
    assert message.type is None
    assert message.is_lc_serializable() is True
    assert str(message) == f"{by}: {content}"


def test_ec_base_chat_message():
    human_message_content = "Hello, how are you?"
    ai_message_content = "I'm fine, thank you!"
    human_metadata = {"user": "John"}
    ai_metadata = {"response_time": 0.5}

    chat_message = ChatMessage()
    chat_message.add_user_message(human_message_content, metadata=human_metadata)
    chat_message.add_ai_message(ai_message_content, metadata=ai_metadata)

    assert chat_message.human_message.content == human_message_content
    assert chat_message.human_message.by == "human"
    assert chat_message.human_message.metadata == human_metadata

    assert chat_message.ai_message.content == ai_message_content
    assert chat_message.ai_message.by == "ai"
    assert chat_message.ai_message.metadata == ai_metadata

    assert str(chat_message) == f"human: {human_message_content} | ai: {ai_message_content}"
