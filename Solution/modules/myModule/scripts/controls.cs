function InputManager::Init_controls(%this)
{
//Create our new ActionMap
new ActionMap(chipmunkcontrols);

chipmunkcontrols.bindCmd(keyboard, "a", "Chippy.turnleft();", "Chippy.stopturn();");
chipmunkcontrols.bindCmd(keyboard, "d", "Chippy.turnright();", "Chippy.stopturn();");
chipmunkcontrols.bindCmd(keyboard, "w", "Chippy.accelerate();", "Chippy.stopthrust();");

//Push our ActionMap on top of the stack
chipmunkcontrols.push();
}