def add_time(start, duration, day=None):
  
  # Check day
  DAYS = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

  if day != None:
    if day.lower() not in DAYS:
      return "Invalid day"

  # Clean start data 
  startdata = start.split()[0]
  starthour = int(startdata.split(':')[0])
  startminutes = int(startdata.split(':')[1])
  ampm = start.split()[1]
  if ampm.lower() == "pm":
    starthour += 12
    if starthour == 24:
      starthour = 0
  
  
  # Clean duration data 
  durationhour = int(duration.split(':')[0])
  durationminutes = int(duration.split(':')[1])
  
  # Get times
  finalminutes = startminutes + durationminutes
  extrahours = int(finalminutes / 60)
  finalminutes = finalminutes % 60
  finalhour = starthour + durationhour + extrahours
  extradays = int(finalhour / 24)
  finalhour = finalhour % 24

  # Fix AMPM 
  if finalhour < 12:
    ampm = 'AM'
  elif finalhour > 12:
    finalhour -= 12
    ampm = 'PM'
  elif finalhour == 12:
    ampm = 'PM'
  
  if finalhour == 0:
    finalhour = 12


  # Get day if requested
  dayindex = 0 
  if day != None:
    dayindex = DAYS.index(day.lower())
    dayindex += extradays
    if dayindex > 6:
      dayindex = dayindex % 7
    dayindex = DAYS[dayindex]

  # Turn every int to str 
  finalhour = str(finalhour)
  finalminutes = str(finalminutes)
  if len(finalminutes) < 2:
    finalminutes = "0"+finalminutes
  dayindex = str(dayindex)

  # Create string with Time 
  new_time = ""
  new_time += finalhour + ':' + finalminutes + ' ' + ampm
  if day != None:
    new_time += ', ' + dayindex.capitalize()
  if extradays == 0:
    return new_time
  elif extradays == 1:
    new_time += ' (next day)'
  else:
    new_time += f' ({extradays} days later)'

  # Return
  return new_time