package internal

import (
	"context"
	"fmt"
	"log"
	"time"
)

type LSM interface {
	Get(ctx context.Context, key string) (int, error)
	Insert(ctx context.Context, key string, value int) error
	Update(ctx context.Context, key string, value int) error
	Delete(ctx context.Context, key string) error
}

type Memtable interface {
	Insert(key string)
}

type LSMImpl struct {
	name                 string
	memtableSizeInB      int
	flushDurationSeconds time.Duration
	Logger               *log.Logger
}

func NewLSM(name string, opts ...Option) LSM {
	impl := defaultLSM()
	impl.name = name
	for _, opt := range opts {
		opt(impl)
	}
	fmt.Printf(`LSM database initialised with
		name: %s,
		memtableSizeInB: %d,
		flushDurationSeconds: %v`, impl.name, impl.memtableSizeInB, impl.flushDurationSeconds)
	return impl
}

func defaultLSM() *LSMImpl {
	return &LSMImpl{
		// 50mb
		memtableSizeInB:      50 * 1024 * 1024,
		flushDurationSeconds: 5 * time.Second,
	}
}

func (impl *LSMImpl) Get(ctx context.Context, key string) (int, error) {
	return 0, nil
}

func (impl *LSMImpl) Insert(ctx context.Context, key string, value int) error {
	return nil
}

func (impl *LSMImpl) Update(ctx context.Context, key string, value int) error {
	return nil
}

func (impl *LSMImpl) Delete(ctx context.Context, key string) error {
	return nil
}
