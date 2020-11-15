package services

import (
	context "context"

	grpc "google.golang.org/grpc"
)

type ProdService struct {
}

func (ps *ProdService) GetProdStock(ctx context.Context, in *ProdRequest, opts ...grpc.CallOption) (*ProdResponse, error) {

	return &ProdResponse{}, nil
}
