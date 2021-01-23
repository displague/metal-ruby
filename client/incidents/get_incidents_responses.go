// Code generated by go-swagger; DO NOT EDIT.

package incidents

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// GetIncidentsReader is a Reader for the GetIncidents structure.
type GetIncidentsReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *GetIncidentsReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewGetIncidentsOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewGetIncidentsUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewGetIncidentsOK creates a GetIncidentsOK with default headers values
func NewGetIncidentsOK() *GetIncidentsOK {
	return &GetIncidentsOK{}
}

/*GetIncidentsOK handles this case with default header values.

ok
*/
type GetIncidentsOK struct {
}

func (o *GetIncidentsOK) Error() string {
	return fmt.Sprintf("[GET /incidents][%d] getIncidentsOK ", 200)
}

func (o *GetIncidentsOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewGetIncidentsUnauthorized creates a GetIncidentsUnauthorized with default headers values
func NewGetIncidentsUnauthorized() *GetIncidentsUnauthorized {
	return &GetIncidentsUnauthorized{}
}

/*GetIncidentsUnauthorized handles this case with default header values.

unauthorized
*/
type GetIncidentsUnauthorized struct {
}

func (o *GetIncidentsUnauthorized) Error() string {
	return fmt.Sprintf("[GET /incidents][%d] getIncidentsUnauthorized ", 401)
}

func (o *GetIncidentsUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
