// Code generated by go-swagger; DO NOT EDIT.

package ports

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// NewAssignPortParams creates a new AssignPortParams object
// with the default values initialized.
func NewAssignPortParams() *AssignPortParams {
	var ()
	return &AssignPortParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewAssignPortParamsWithTimeout creates a new AssignPortParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewAssignPortParamsWithTimeout(timeout time.Duration) *AssignPortParams {
	var ()
	return &AssignPortParams{

		timeout: timeout,
	}
}

// NewAssignPortParamsWithContext creates a new AssignPortParams object
// with the default values initialized, and the ability to set a context for a request
func NewAssignPortParamsWithContext(ctx context.Context) *AssignPortParams {
	var ()
	return &AssignPortParams{

		Context: ctx,
	}
}

// NewAssignPortParamsWithHTTPClient creates a new AssignPortParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewAssignPortParamsWithHTTPClient(client *http.Client) *AssignPortParams {
	var ()
	return &AssignPortParams{
		HTTPClient: client,
	}
}

/*AssignPortParams contains all the parameters to send to the API endpoint
for the assign port operation typically these are written to a http.Request
*/
type AssignPortParams struct {

	/*ID
	  Port UUID

	*/
	ID strfmt.UUID
	/*Vnid
	  Virtual Network ID

	*/
	Vnid *types.PortAssignInput

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the assign port params
func (o *AssignPortParams) WithTimeout(timeout time.Duration) *AssignPortParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the assign port params
func (o *AssignPortParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the assign port params
func (o *AssignPortParams) WithContext(ctx context.Context) *AssignPortParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the assign port params
func (o *AssignPortParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the assign port params
func (o *AssignPortParams) WithHTTPClient(client *http.Client) *AssignPortParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the assign port params
func (o *AssignPortParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the assign port params
func (o *AssignPortParams) WithID(id strfmt.UUID) *AssignPortParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the assign port params
func (o *AssignPortParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WithVnid adds the vnid to the assign port params
func (o *AssignPortParams) WithVnid(vnid *types.PortAssignInput) *AssignPortParams {
	o.SetVnid(vnid)
	return o
}

// SetVnid adds the vnid to the assign port params
func (o *AssignPortParams) SetVnid(vnid *types.PortAssignInput) {
	o.Vnid = vnid
}

// WriteToRequest writes these params to a swagger request
func (o *AssignPortParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if o.Vnid != nil {
		if err := r.SetBodyParam(o.Vnid); err != nil {
			return err
		}
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
