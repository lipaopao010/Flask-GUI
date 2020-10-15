// name a few variables

const inputModelFile = document.querySelector("#modelfile");
const modelmessage = document.querySelector("#modelmessage");
const inputBlastFile = document.querySelector("#blastfile");
const blastmessage = document.querySelector("#blastmessage");
inputModelFile.addEventListener("change", updateModelFile);
inputBlastFile.addEventListener("change", updateBlastFile);

// function to get the uploaded model file name:

function getModelFileName() {
  const file = inputModelFile.files;
  //console.log(file[0]);
  const nameArray = file[0].name.split(".");
  //console.log(nameArray);
  const modelFileName = nameArray[0];
  return modelFileName;
}

// function to get the blast file name

function getBlastFileName() {
  const file = inputBlastFile.files;
  //console.log(file[0]);
  const nameArray = file[0].name.split(".");
  //console.log(nameArray);
  const blastFileName = nameArray[0];
  return blastFileName;
}

// function to get the uploaded model file type

function getModelFileType() {
  const file = inputModelFile.files;
  const fileTypeModel = file[0].name.split(".").pop();
  return fileTypeModel;
}

// function to get the uploaded model file type

function getBlastFileType() {
  const file = inputBlastFile.files;
  const fileTypeBlast = file[0].name.split(".").pop();
  return fileTypeBlast;
}

// Function to upload the model file

function updateModelFile() {
  // clear the previous file name
  while (modelmessage.firstChild) {
    modelmessage.removeChild(modelmessage.firstChild);
  }

  const modelFileName = getModelFileName();
  const fileTypeModel = getModelFileType();

  const para = document.createElement("p");

  // if filename is empty
  if (!modelFileName) {
    para.textContent = "No files currently selected for upload";
  } else if (fileTypeModel !== "csv") {
    // if file type is not csv, pop up message of incorrect file type
    para.textContent = "File type is not correct, please upload a csv file!";
    // message of sweet alert
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "File type is wrong!",
    });
  } else if (modelFileName === "block_model") {
    // if the file name matches block_model, showing the message of successful upload
    console.log(modelFileName);
    para.textContent = `File name ${modelFileName} successfully uploaded! `;

    //message of sweet alert
    Swal.fire({
      icon: "success",
      title: "Great!",
      text: "Your model file is uploaded successfully!",
    });
  } else {
    // if file name doesn't match, show the message of file name incorrect
    para.textContent = `File name ${modelFileName} . Please upload the correct file!`;
    // sweet alert message
    Swal.fire({
      icon: "error",
      title: "File name is not right",
      text: "Please upload the correct file!",
    });
  }
  // put the message into the text of message area
  modelmessage.appendChild(para);
}


// FUNCTION OF UPLOADING BLAST FILE
function updateBlastFile() {
  // clear the previous file name
  while (blastmessage.firstChild) {
    blastmessage.removeChild(blastmessage.firstChild);
  }

  const blastFileName = getBlastFileName();
  const fileTypeBlast = getBlastFileType();
  const para = document.createElement("p");

  if (!blastFileName) {
    para.textContent = "No files currently selected for upload";
  } else if (fileTypeBlast !== "csv") {
    para.textContent = "File type is not correct, please upload a csv file!";
    //message of sweet alert
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "File type is wrong!",
    });
  } else if (blastFileName !== "Blast_design") {
    para.textContent = `File name ${blastFileName} . Please upload the correct file!`;
    //message of sweet alert
    Swal.fire({
      icon: "error",
      title: "File name is not right",
      text: "Please upload the correct file!",
    });
  } else {
    para.textContent = `File name ${blastFileName} successfully uploaded !`;

    //message of sweet alert
    Swal.fire({
      icon: "success",
      title: "Great!",
      text: "Your blast file is uploaded successfully!",
    });
  }
  blastmessage.appendChild(para);
}

// run terminal after clicking "run program" button
// if the files are not correct, the program cannot run
function runProgram() {
  const file1 = getModelFileName();
  console.log(file1);
  const file2 = getBlastFileName();
  console.log(file2);
  // both file names need to match to show the correct message
  if (file1 == "block_model" && file2 == "Blast_design") {
    console.log("both files are correct!");
    //message of sweet alert
    Swal.fire({
      icon: "success",
      title: "Great!",
      text: "File executed successfully in terminal !",
    });

    window.location.href = '/run';
  } else {
    console.log("something is wrong !");
    //message of sweet alert
    Swal.fire({
      icon: "error",
      title: "something is wrong",
      text: "Please make sure you upload the correct files !",
    });
  }
}
