object "Solver" {
    code {
        // deploy the contract
        datacopy(0, dataoffset("runtime"), datasize("runtime"))
        return(0, datasize("runtime"))
    }
    object "runtime" {
        code {
            mstore(0, 42)
            return(0, 32)
        }
    }
}
