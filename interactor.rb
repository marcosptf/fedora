
def callBlock
  yield
  yield
end

callBlock{ puts("print it in the block") }


