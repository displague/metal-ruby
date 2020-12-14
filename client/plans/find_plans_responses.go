// Code generated by go-swagger; DO NOT EDIT.

package plans

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// FindPlansReader is a Reader for the FindPlans structure.
type FindPlansReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindPlansReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindPlansOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindPlansUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindPlansOK creates a FindPlansOK with default headers values
func NewFindPlansOK() *FindPlansOK {
	return &FindPlansOK{}
}

/*FindPlansOK handles this case with default header values.

ok
*/
type FindPlansOK struct {
	Payload *models.PlanList
}

func (o *FindPlansOK) Error() string {
	return fmt.Sprintf("[GET /plans][%d] findPlansOK  %+v", 200, o.Payload)
}

func (o *FindPlansOK) GetPayload() *models.PlanList {
	return o.Payload
}

func (o *FindPlansOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.PlanList)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindPlansUnauthorized creates a FindPlansUnauthorized with default headers values
func NewFindPlansUnauthorized() *FindPlansUnauthorized {
	return &FindPlansUnauthorized{}
}

/*FindPlansUnauthorized handles this case with default header values.

unauthorized
*/
type FindPlansUnauthorized struct {
}

func (o *FindPlansUnauthorized) Error() string {
	return fmt.Sprintf("[GET /plans][%d] findPlansUnauthorized ", 401)
}

func (o *FindPlansUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}