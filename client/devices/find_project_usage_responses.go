// Code generated by go-swagger; DO NOT EDIT.

package devices

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// FindProjectUsageReader is a Reader for the FindProjectUsage structure.
type FindProjectUsageReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindProjectUsageReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindProjectUsageOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindProjectUsageUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewFindProjectUsageNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindProjectUsageOK creates a FindProjectUsageOK with default headers values
func NewFindProjectUsageOK() *FindProjectUsageOK {
	return &FindProjectUsageOK{}
}

/*FindProjectUsageOK handles this case with default header values.

ok
*/
type FindProjectUsageOK struct {
	Payload *types.ProjectUsageList
}

func (o *FindProjectUsageOK) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/usages][%d] findProjectUsageOK  %+v", 200, o.Payload)
}

func (o *FindProjectUsageOK) GetPayload() *types.ProjectUsageList {
	return o.Payload
}

func (o *FindProjectUsageOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.ProjectUsageList)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindProjectUsageUnauthorized creates a FindProjectUsageUnauthorized with default headers values
func NewFindProjectUsageUnauthorized() *FindProjectUsageUnauthorized {
	return &FindProjectUsageUnauthorized{}
}

/*FindProjectUsageUnauthorized handles this case with default header values.

unauthorized
*/
type FindProjectUsageUnauthorized struct {
}

func (o *FindProjectUsageUnauthorized) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/usages][%d] findProjectUsageUnauthorized ", 401)
}

func (o *FindProjectUsageUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindProjectUsageNotFound creates a FindProjectUsageNotFound with default headers values
func NewFindProjectUsageNotFound() *FindProjectUsageNotFound {
	return &FindProjectUsageNotFound{}
}

/*FindProjectUsageNotFound handles this case with default header values.

not found
*/
type FindProjectUsageNotFound struct {
}

func (o *FindProjectUsageNotFound) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/usages][%d] findProjectUsageNotFound ", 404)
}

func (o *FindProjectUsageNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
