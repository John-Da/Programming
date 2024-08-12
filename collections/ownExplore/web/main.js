function sleepIn(weekday, vacation) {
    return !weekday || vacation;
  }
  
  // Examples
  console.log(sleepIn(false, false));  // Output: true
  console.log(sleepIn(true, false));   // Output: false
  console.log(sleepIn(false, true));   // Output: true
  