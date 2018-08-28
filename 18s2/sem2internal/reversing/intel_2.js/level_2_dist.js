function runIntel(program) {
  var ramSize = 255;
  var ram = Array.from(Array(255)).map((arg, index) => 0);
  // i'm so clever, use this 1 to mark the end of memory
  ram[255] = 1;
  var register = [0,0,0,0,0,0,0,0];
  var instructions = {
    "READ": (args) => register[args[0]] = ram[args[1]],
    "SHOW": (args) => console.log(String.fromCharCode(register[args[0]])),
    "SUB": (args) => register[args[0]] = register[args[1]] - register[args[2]],
    "WRITE": (args) => ram[args[0]] = register[args[1]],
    "DEBUG": (args) => console.log(register)
  }
  for (let instruction of program) {
    let i = instruction.split(" ")[0];
    if (instructions[i] === undefined) continue;
    let args = instruction.split(" ").slice(1);
    args = args.map(x => parseInt(x));
    instructions[i](args);
  }
  let secretMemory = "flag{XXXXXXXXXXXXX}";
  if (register[0] == 50) console.log(secretMemory);
}

process.stdin.on('data', function (data) {
  let program = String(data).split("\n");
  runIntel(program.slice(0,-1));
});
