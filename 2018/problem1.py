#Ben Carlson
import sys

def main():
  out = problem()
  for i in range(len(out)):
    print("Case #" + str(i + 1) + ": " + out[i])
  sys.stdout.flush()

def problem():
  num = int(input())
  out = []
  for i in range(num):
    line = input()
    damage, commands = line.split(" ")
    damage = int(damage)
    count = 0
    dam = calc_damage(commands)
    if dam <= damage:
      out.append(str(count))
      continue
    flag = True
    for i in range(len(commands) - 2, -1, -1):
      for j in range(i, -1, -1):
        if commands[j] == "C":
          pos = j
          while pos + 1 < len(commands) and commands[pos + 1] != "C":
            commands = commands[:pos] + commands[pos + 1] + commands[pos] + commands[pos + 2:]
            count += 1
            dam = calc_damage(commands)
            if dam <= damage:
              out.append(str(count))
              flag = False
              break
            pos += 1
        if not flag:
          break
      if not flag:
        break
    if flag:
      out.append("IMPOSSIBLE")
  return out

def calc_damage(commands):
  dam = 1
  tot = 0
  for i in commands:
    if i == "S":
      tot += dam
    else:
      dam *= 2
  return tot

main()


