from text_system import TextContext, TextElement


def test_add_and_remove_elements():
    ctx = TextContext()
    elem1 = TextElement("child", parent=ctx.root)
    ctx.root.add_child(elem1)

    assert len(ctx.root.children) == 1
    assert ctx.root.children[0].name == "child"

    ctx.root.remove_child("child")
    assert len(ctx.root.children) == 0


def test_pwd_and_navigation():
    ctx = TextContext()
    elem = TextElement("section", parent=ctx.root)
    ctx.root.add_child(elem)
    ctx.current = elem

    assert ctx.pwd() == "/root/section"
