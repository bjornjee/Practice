package internal

import (
	"log"
	"time"
)

type Option func(impl *LSMImpl) *LSMImpl

func WithFlushDurationSeconds(duration time.Duration) Option {
	return func(impl *LSMImpl) *LSMImpl {
		impl.flushDurationSeconds = duration
		return impl
	}
}

func WithMemtableSizeInB(size int) Option {
	return func(impl *LSMImpl) *LSMImpl {
		impl.memtableSizeInB = size
		return impl
	}
}

func WithLogger(logger *log.Logger) Option {
	return func(impl *LSMImpl) *LSMImpl {
		impl.logger = logger
		return impl
	}
}
