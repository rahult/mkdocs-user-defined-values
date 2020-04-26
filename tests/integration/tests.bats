##
# These are helper variables and functions written in Bash. It's like writing in your Terminal!
# Feel free to optimize these, or even run them in your own Terminal.
#

rootDir=$(pwd)
fixturesDir=${rootDir}/tests/integration

debugger() {
  echo "--- STATUS ---"
  if [ $status -eq 0 ]
  then
    echo "Successful Status Code ($status)"
  else
    echo "Failed Status Code ($status)"
  fi
  echo "--- OUTPUT ---"
  echo $output
  echo "--------------"
}

assertFileExists() {
  run cat $1
  [ "$status" -eq 0 ]
}

assertSuccessMkdocs() {
  run pipenv run mkdocs $@
  debugger
  assertFileExists output/page_with_plugin.html
  [ "$status" -eq 0 ]
}

assertFailedMkdocs() {
  run pipenv run mkdocs $@
  debugger
  [ "$status" -ne 0 ]
}

##
# These are special lifecycle methods for Bats (Bash automated testing).
# setup() is ran before every test, teardown() is ran after every test.
#

teardown() {
  rm -rf ${fixturesDir}/*/output
}

##
# Test suites.
#

@test "builds a mkdocs site with minimal configuration" {
  cd ${fixturesDir}/demo
  assertSuccessMkdocs build --clean -d output
}
