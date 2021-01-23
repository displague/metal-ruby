// Code generated by go-swagger; DO NOT EDIT.

package batches

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// DeleteBatchReader is a Reader for the DeleteBatch structure.
type DeleteBatchReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *DeleteBatchReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 204:
		result := NewDeleteBatchNoContent()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 403:
		result := NewDeleteBatchForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewDeleteBatchNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewDeleteBatchNoContent creates a DeleteBatchNoContent with default headers values
func NewDeleteBatchNoContent() *DeleteBatchNoContent {
	return &DeleteBatchNoContent{}
}

/*DeleteBatchNoContent handles this case with default header values.

no content
*/
type DeleteBatchNoContent struct {
}

func (o *DeleteBatchNoContent) Error() string {
	return fmt.Sprintf("[DELETE /batches/{id}][%d] deleteBatchNoContent ", 204)
}

func (o *DeleteBatchNoContent) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewDeleteBatchForbidden creates a DeleteBatchForbidden with default headers values
func NewDeleteBatchForbidden() *DeleteBatchForbidden {
	return &DeleteBatchForbidden{}
}

/*DeleteBatchForbidden handles this case with default header values.

forbidden
*/
type DeleteBatchForbidden struct {
}

func (o *DeleteBatchForbidden) Error() string {
	return fmt.Sprintf("[DELETE /batches/{id}][%d] deleteBatchForbidden ", 403)
}

func (o *DeleteBatchForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewDeleteBatchNotFound creates a DeleteBatchNotFound with default headers values
func NewDeleteBatchNotFound() *DeleteBatchNotFound {
	return &DeleteBatchNotFound{}
}

/*DeleteBatchNotFound handles this case with default header values.

not found
*/
type DeleteBatchNotFound struct {
}

func (o *DeleteBatchNotFound) Error() string {
	return fmt.Sprintf("[DELETE /batches/{id}][%d] deleteBatchNotFound ", 404)
}

func (o *DeleteBatchNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
