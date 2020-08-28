import codeanticode.eliza.*;

Eliza eliza;
eliza = new Eliza(this);

String response = eliza.processInput("Hello");
println(response);