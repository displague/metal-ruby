// Code generated by go-swagger; DO NOT EDIT.

package projects

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// FindBatchesByProjectReader is a Reader for the FindBatchesByProject structure.
type FindBatchesByProjectReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindBatchesByProjectReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindBatchesByProjectOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindBatchesByProjectUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewFindBatchesByProjectForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewFindBatchesByProjectNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindBatchesByProjectOK creates a FindBatchesByProjectOK with default headers values
func NewFindBatchesByProjectOK() *FindBatchesByProjectOK {
	return &FindBatchesByProjectOK{}
}

/*FindBatchesByProjectOK handles this case with default header values.

ok
*/
type FindBatchesByProjectOK struct {
	Payload *types.BatchesList
}

func (o *FindBatchesByProjectOK) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/batches][%d] findBatchesByProjectOK  %+v", 200, o.Payload)
}

func (o *FindBatchesByProjectOK) GetPayload() *types.BatchesList {
	return o.Payload
}

func (o *FindBatchesByProjectOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.BatchesList)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindBatchesByProjectUnauthorized creates a FindBatchesByProjectUnauthorized with default headers values
func NewFindBatchesByProjectUnauthorized() *FindBatchesByProjectUnauthorized {
	return &FindBatchesByProjectUnauthorized{}
}

/*FindBatchesByProjectUnauthorized handles this case with default header values.

unauthorized
*/
type FindBatchesByProjectUnauthorized struct {
}

func (o *FindBatchesByProjectUnauthorized) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/batches][%d] findBatchesByProjectUnauthorized ", 401)
}

func (o *FindBatchesByProjectUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindBatchesByProjectForbidden creates a FindBatchesByProjectForbidden with default headers values
func NewFindBatchesByProjectForbidden() *FindBatchesByProjectForbidden {
	return &FindBatchesByProjectForbidden{}
}

/*FindBatchesByProjectForbidden handles this case with default header values.

forbidden
*/
type FindBatchesByProjectForbidden struct {
}

func (o *FindBatchesByProjectForbidden) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/batches][%d] findBatchesByProjectForbidden ", 403)
}

func (o *FindBatchesByProjectForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindBatchesByProjectNotFound creates a FindBatchesByProjectNotFound with default headers values
func NewFindBatchesByProjectNotFound() *FindBatchesByProjectNotFound {
	return &FindBatchesByProjectNotFound{}
}

/*FindBatchesByProjectNotFound handles this case with default header values.

not found
*/
type FindBatchesByProjectNotFound struct {
}

func (o *FindBatchesByProjectNotFound) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/batches][%d] findBatchesByProjectNotFound ", 404)
}

func (o *FindBatchesByProjectNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
