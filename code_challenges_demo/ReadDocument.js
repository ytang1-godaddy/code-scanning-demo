/*********************
 * Difficulty ★★☆☆☆
 ********************/
const express = require("express");
const db = require("./SQLConnector");

// Setup Express Server
const app = express();
app.use(express.json());

// Return `true` if permission allowed, `false` if not.
app.post("/checkPermission", async (request, response) => {
  const { req_docID, req_email } = request.body;
  const sqlQuery = `SELECT *` +
                   `FROM docs_with_owner` +
                   `WHERE id = '${req_docID}' AND owner = '${req_email}'`;
  try {
    const result = await db.query(sqlQuery);
    if (result.length !== 0) {
      response.json({ authorized: true });
    } else {
      response.json({ authorized: false });
    }
  } catch (err) {
    throw err;
  }
});

app.listen(3000, () => {
  console.log("My API listening on port 3000");
});
