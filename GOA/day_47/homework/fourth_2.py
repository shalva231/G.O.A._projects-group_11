def find_largest(a, b, c, d, e):
  if a > b:
    if a > c:
      if a > d:
        if a > e:
          return a
        elif e > a:
          return e
      elif d > c:
        if d > e:
          return d
        elif e > d:
          return e
    elif c > a:
      if c > d:
        if c > e:
          return c
        elif e > c:
          return e
        
    elif b > a:
      if b > c:
        if b > d:
          if b > e:
            return b
          elif e > b:
            return e
        elif d > c:
          if d > e:
            return d
          elif e > d:
            return e
      elif c > a:
        if c > d:
          if c > e:
            return c
          elif e > c:
            return e
      elif d > a:
        if d > c:
          if d > e:
            return d
          elif e > d:
            return e
      elif e > a:
        if e > c:
          if e > d:
            return e
          elif d > e:
            return d
        elif c > a:
          if c > d:
            if c > e:
              return c
            elif e > c:
              return e
          elif d > c:
            if d > e:
              return d
            elif e > d:
              return e
      