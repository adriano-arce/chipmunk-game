function createChippy()
{
    %chipmunk = new Sprite(Chippy);
    %chipmunk.setBodyType( dynamic );
    %chipmunk.Position = "0 0";
    %chipmunk.Size = "4 4";
    %chipmunk.SceneLayer = 1;
    %chipmunk.Image = "myModule:Chippy";
    %chipmunk.createPolygonBoxCollisionShape();
    %chipmunk.setCollisionCallback(true);
    %chipmunk.setFixedAngle(true);
    %chipmunk.isThrusting = false;
    myScene.add(%chipmunk);
}

function Chippy::onCollision(%this, %sceneobject, %collisiondetails)
{
  if(%sceneobject.getSceneGroup() == 20)
  {
    %sceneobject.safedelete();
    createacorns(1);  
  }
}

function Chippy::accelerate(%this)  
{  
    %adjustedAngle = %this.Angle + 90;  
    %adjustedAngle %= 360;  
    if(%this.isThrusting)  
    {    
        %ThrustVector= Vector2Direction(%adjustedAngle,35);  
    }  
    else  
    {  
        %ThrustVector = Vector2Direction(%adjustedAngle,95);  
        %this.setLinearDamping(0.0);    
        %this.setAngularDamping(30.0);  
    }  
 
    %MywordX = %this.Position.x + %ThrustVector.x;  
    %MywordY = %this.Position.y + %ThrustVector.y;    
    %this.applyLinearImpulse(%ThrustVector, "0 0");  
    %this.isThrusting = true;  
    %this.thrustschedule = %this.schedule(100,accelerate);     
}

function Chippy::turnleft(%this)
{
    %this.setAngularVelocity(300);
    %this.turnschedule = %this.schedule(50,turnleft);
}

function Chippy::turnright(%this)
{
    %this.setAngularVelocity(-300);
    %this.turnschedule = %this.schedule(50,turnright);
}

function Chippy::stopturn(%this)
{
   cancel(%this.turnschedule);
   %this.setAngularVelocity(0);
}

function Chippy::stopthrust(%this)
{ 
    %this.setLinearVelocity(0,0);
    %this.setAngularDamping(0.0);
    cancel(%this.thrustschedule);
    %this.isThrusting = false;
}