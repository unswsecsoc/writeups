// maybe minify this to make it harder?
function runIntel(program) {
  var ramSize = 4096;
  var ram = Array.from(Array(ramSize)).map((arg, index) => 0);
  var i = 0;
  for(let instruction of program) {
    ram[i] = instruction;
    i++;
  }
  // put flag in protected section of ram
  var i = 4001;
  for(let c of "flag{ooOOOooOOOooOOOOoo}") {
    ram[i] = c.charCodeAt(0);
    i++;
  }
  var register = [0,0,0,0,0,0,0,0];
  var instructions = [
    (a,b,c) => {},
    (a,b,c) => {if (b < 4000) register[a] = ram[b]},
    (a,b,c) => console.log(String.fromCharCode(register[a])),
    (a,b,c) => register[a] = register[b] - register[c],
    (a,b,c) => register[a] = register[b] + register[c],
    (a,b,c) => {if (a < 4000) ram[a] = register[b]},
    (a,b,c) => console.log(register),
    (a,b,c) => register[a] = b,
    (a,b,c) => register[a] = ram[b] + ram[c]
  ];
  let pc = 0;
  while(pc+3 <= 4000) {
    if (instructions[ram[pc]] !== undefined)
      instructions[ram[pc]](ram[pc+1],ram[pc+2],ram[pc+3]);
    pc+=4;
  }
}

process.stdin.on('data', function (data) {
  let program = String(data).split(" ");
  program = program.map(x => parseInt(x));
  runIntel(program);
});
console.log("Welcome to intel_3.js! Good luck with this one smarty pants");
