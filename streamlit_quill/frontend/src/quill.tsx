import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection
} from "streamlit-component-lib";
import React, { useEffect, useRef } from "react"
import ReactQuill from "react-quill"
import ResizeObserver from "resize-observer-polyfill"
import katex from "katex"

import "katex/dist/katex.min.css"
import "quill/dist/quill.snow.css"

interface QuillProps extends ComponentProps {
  args: any
}

const Quill = ({ args }: QuillProps) => {
  const divRef = useRef<HTMLDivElement>(null)

  let timeout: NodeJS.Timeout

  const handleChange = (content: string, delta: any, source: any, editor: any) => {
    clearTimeout(timeout)
    timeout = setTimeout(() => {
      Streamlit.setComponentValue(args.html ? content : editor.getText())
    }, 200)
  }

  useEffect(() => {
    Streamlit.setFrameHeight()

    window.katex = katex

    const ro = new ResizeObserver(() => {
      Streamlit.setFrameHeight()
    })

    if (divRef.current)
      ro.observe(divRef.current)

    return () => ro.disconnect()
  })

  return <div ref={divRef}>
    <ReactQuill
      defaultValue={args.defaultValue}
      modules={{
        toolbar: args.toolbar,
        history: args.history,
      }}
      placeholder={args.placeholder}
      preserveWhitespace={args.preserveWhitespace}
      readOnly={args.readOnly}
      onChange={handleChange}
    />
  </div>
}

export default withStreamlitConnection(Quill)
