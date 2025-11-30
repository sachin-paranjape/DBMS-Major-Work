# Topic 6 – Demonstration of NoSQL and Comparison with RDBMS (MongoDB)
# Tools Used
- MongoDB Community Server
- MongoDB Shell (mongosh)
- MongoDB Compass
# Database and Collection Creation
```js
use studentDB
db.createCollection("students")

Insert Operation (CREATE)
db.students.insertOne({
  name: "Vaibhav",
  branch: "CSE",
  skills: ["DBMS", "Python"]
})

Read Operation (READ)
db.students.find()
db.students.find({ branch: "CSE" })
Update Operation (UPDATE)
db.students.updateOne(
  { name: "Vaibhav" },
  { $set: { branch: "AIML" } }
)

Delete Operation (DELETE)
db.students.deleteOne({ name: "Vaibhav" })