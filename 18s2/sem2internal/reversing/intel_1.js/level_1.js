var ramSize = 255;
var ram = Array.from(Array(255)).map((arg, index) => 0);
var register;
let x = 0;
flag = "flag{0ne_r3g1st3r_1s_m0r3_th3n_3n0ugh}";
for(x=0;x<flag.length;x++){
  ram[128+x] = flag.charCodeAt(x);
}

function runIntel(program) {
  var instructions = {
    "READ": (args) => register = ram[args[0]],
    "SHOW": () => console.log(String.fromCharCode(register))
  }
  for (let instruction of program) {
    let i = instruction.split(" ")[0];
    let args = instruction.split(" ").slice(1);
    try{
      instructions[i](args);
    } catch(e){

    }
  }
}

process.stdin.on('data', function (data) {
  runIntel(String(data).split("\n"));
});
console.log("Welcome to intel_1.js! Write some code why don't cha");
