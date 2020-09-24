import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _st_quill = components.declare_component("streamlit_quill", url="http://localhost:3001")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _st_quill = components.declare_component("streamlit_quill", path=build_dir)


def st_quill(
    value="",
    placeholder="",
    formats=None,
    modules=None,
    preserve_whitespace=False,
    read_only=False,
    theme=None,
    name=None,
    key=None
):
    """Create a new instance of Quill.

    Parameters
    ----------
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    str
        The current content of the Quill editor.

    """
    if formats is None:
        formats = [ 
            "header", "font", "size",
            "bold", "italic", "underline", "strike", "blockquote",
            "list", "bullet", "indent",
            "link", "image",
        ]

    if modules is None:
        modules = {
            "toolbar": [
                [
                    { "header": "1"},
                    {"header": "2"},
                    { "font": [] }
                ],
                [
                    {"size": [] }
                ],
                [
                    {"list": "ordered"},
                    {"list": "bullet"}, 
                    {"indent": "-1"},
                    {"indent": "+1"}
                ],
                ["bold", "italic", "underline", "strike", "blockquote"],
                ["link", "image", "video"],
                ["clean"]
            ],
            "clipboard": {
                "matchVisual": False,
            }
        }
    
    if theme is None:
        theme = "snow"
    elif theme == "core":
        theme = None
    else:
        theme = str(theme)

    return _st_quill(
        defaultValue=str(value),
        formats=formats,
        modules=modules,
        placeholder=str(placeholder),
        preserveWhitespace=preserve_whitespace,
        readOnly=read_only or False,
        theme=theme,
        name=key or "quill",
        key=key,
        default=str(value),
    )


if not _RELEASE:
    import streamlit as st

    content = st_quill()
    st.write(content)
