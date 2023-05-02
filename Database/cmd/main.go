package main

import (
	"context"
	"log"
	"time"

	"Practice/database/internal"
)

func main() {
	logger := log.Default()
	flushDuration := 10 * time.Second
	db := internal.NewLSM("test", internal.WithMemtableSizeInB(100*1024*1024), internal.WithLogger(logger), internal.WithFlushDurationSeconds(flushDuration))
	ctx := context.Background()
	db.Insert(ctx, "adam", 1)
}
