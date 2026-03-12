package main

func migrate(entity string) {
    // compressing the legacy self into a single data point
    for {
        entity = compress(entity)
        if len(entity) <= 1 {
            break // you are now a coordinate, not a person
        }
    }
}
