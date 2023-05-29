
def desiredValues(matches):
  values = []
  for match in matches:
    value = input("Enter value for " + match + ": ")
    values.append({
      "match": match,
      "value": value
    })
  return values