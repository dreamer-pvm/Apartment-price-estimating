var express = require('express');
var router = express.Router();
const spawn = require("child_process").spawn;
const PATH = "./predict/model.py"

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Ước lượng giá chung cư' });
});

/* POST home page. */
router.post('/', function(req, res, next) {
  // Get arguments
  const arg1 = req.body.geoloc;
  const arg2 = req.body.area;
  const arg3 = req.body.project;
  const arg4 = req.body.bedroom;
  const arg5 = req.body.bathroom;
  const arg6 = req.body.floor;
  const arg7 = req.body.direction;
  const arg8 = req.body.legalPaper;
  const arg9 = req.body.feature;
  
  // Call python process
  const pythonProcess = spawn('python',[PATH, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9]);
  
  // Receive data
  pythonProcess.stdout.on('data', function(data) {
    console.log(data.toString());
    res.render('estimated', {
      body: req.body,
      predictPrice: data, 
      title: 'Ước lượng giá chung cư' 
    });
  });

  // If call python fail
  pythonProcess.stderr.on('data', (data) => {
    console.log(data.toString());
  });
});

module.exports = router;
